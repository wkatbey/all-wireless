from django.shortcuts import render, redirect
from django.views.generic import TemplateView, View
from static_website.forms import ContactForm
from django.core.mail import send_mail

COMPANY_EMAIL = 'allwirelessinc@att.net'
DEFAULT_SUBJECT = 'Website Email'

class Home(View):
    template_name = 'static_website/index.html'

    def get(self, request):
        form = ContactForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        context = {}
        form = ContactForm(request.POST)

        if form.is_valid():
            message = form.cleaned_data['inquiry']
            from_email = form.cleaned_data['email']
            full_name = form.cleaned_data['first_name'] + ' ' + form.cleaned_data['last_name']
            subject = full_name + ': ' + DEFAULT_SUBJECT

            content = "text/plain", "Hello, Email!"

            send_mail(subject, message, from_email, [COMPANY_EMAIL], fail_silently=True)
     
            form = ContactForm()

            context['form'] = form
            context['message'] = "We appreciate your inquiry! A member of our team will respond as soon as they can"

            return redirect(request.path)

        form = ContactForm()
        return redirect(request.path)

