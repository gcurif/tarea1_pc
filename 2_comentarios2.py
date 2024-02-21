"""
        print("esta es otra forma de no hacer nada, con 3 comilla")
        forms = [form.cleaned_data for form in form_list]
        data = forms[0]
        documents_data = forms[1]

        # save commune
        commune = data['commune']
        if commune:
            data['commune'] = commune.id
        else:
            data['commune'] = None

        # save documents
        file_data = {}
        file_data['deed_of_constitution'] = (
            documents_data.get('deed_of_constitution')
        )
        file_data['authorized_copy_of_societys_statutes'] = (
            documents_data.get('authorized_copy_of_societys_statutes')
        )

        # get user
        user = self.request.user

        company_form = CompanyForm(data, file_data, instance=self.company)

        if company_form.is_valid():
            # Legal representative
            legal_representative = None
            if not documents_data.get('is_legal_representative'):
                # A new user for the company's legal representative is created
                rut = documents_data.get('user_rut')
                if rut:
                    try:
                        legal_representative = User.objects.get(
                            rut=format_rut(rut)
                        )
                    except User.DoesNotExist:
                        pass

                if not legal_representative:
                    legal_representative = User.objects.create(
                        first_name=documents_data.get('user_first_name'),
                        last_name=documents_data.get('user_last_name'),
                        email=documents_data.get('user_email'),
                        rut=format_rut(documents_data.get('user_rut')),
                        address=documents_data.get('user_address'),
                    )
                elif legal_representative.first_name == "Invitado":
                    legal_representative.update(
                        first_name=documents_data.get('user_first_name'),
                        last_name=documents_data.get('user_last_name'),
                        email=documents_data.get('user_email'),
                        address=documents_data.get('user_address'),
                    )

            else:
                # Use the request user for the company's legal representative
                legal_representative = user

                email = documents_data.get('request_user_email')
                if email:
                    user.email = email
                    user.address = documents_data.get(
                        'request_user_address'
                    )
                    user.save()

            company = company_form.save()
            company.update(status=CompanyStatuses.ENTERED)
            self.object = company

            if legal_representative != user:
                company.companymembership_set.create(
                    user=legal_representative,
                    #is_legal_representative=True,
                )
                company.companymembership_set.create(user=user)
            else:
                company.companymembership_set.create(
                    user=user,
                    #is_legal_representative=True,
                )

            company.send_creation_email()

            return HttpResponseRedirect(self.get_success_url())

"""