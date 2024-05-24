from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm
from django.views.generic.edit import FormView
from django.urls import reverse_lazy


# Create your views here.
class ContactFormView(FormView):
    template_name = 'index.html'
    form_class = ContactForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.save()
        messages.success(self.request, "Message Sent Successfully!")
        return super().form_valid(form)

def get_context_data(self, **kwargs):
        context = super(ContactFormView, self).get_context_data(**kwargs)
        context['messages'] = messages.get_messages(self.request)
        return context