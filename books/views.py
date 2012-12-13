from django.views.generic import CreateView, ListView, DetailView
from django.shortcuts import redirect, get_object_or_404
from .models import Book, Author
from .forms import AuthorForm, BookFormSet


class ManageBooksView(CreateView):
    template_name = 'books/author_and_books_form.html'
    form_class = AuthorForm

    def get_context_data(self, **kwargs):
        context = super(ManageBooksView, self).get_context_data(**kwargs)
        instance = None
        author_pk = self.kwargs.get('pk')
        if author_pk:
            instance = get_object_or_404(Author, pk=author_pk)
        if self.request.POST:
            context['form'] = AuthorForm(self.request.POST, instance=instance)
            context['formset'] = BookFormSet(self.request.POST, instance=instance)
        else:
            context['form'] = AuthorForm(instance=instance)
            context['formset'] = BookFormSet(instance=instance)
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        form = context['form']
        formset = context['formset']
        if form.is_valid() and formset.is_valid():
            self.object = form.save()
            formset.instance = self.object
            formset.save()
            return redirect(self.object.get_absolute_url())
        else:
            return self.render_to_response(self.get_context_data(form=form))

manage_books = ManageBooksView.as_view()


class BookList(ListView):

    model = Book

book_list = BookList.as_view()


class BookDetail(DetailView):

    model = Book

book_detail = BookDetail.as_view()


class AuthorList(ListView):

    model = Author

author_list = AuthorList.as_view()


class AuthorDetail(DetailView):

    model = Author

author_detail = AuthorDetail.as_view()
