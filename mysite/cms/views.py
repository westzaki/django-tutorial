from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.views.generic.list import ListView
from cms.forms import BookForm, ImpressionForm
from cms.models import Book, Impression

def book_list(request):
    books = Book.objects.all().order_by('id')
    return render_to_response('cms/book_list.html',
                              {'books': books},
                              context_instance=RequestContext(request))

def book_edit(request, book_id=None):
    if book_id:
        book = get_object_or_404(Book, pk=book_id)
    else:
        book = Book()

    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            book = form.save(commit=False)
            book.save()
            return redirect('cms:book_list')
    else:
        form = BookForm(instance=book)

    return render_to_response('cms/book_edit.html',
                              dict(form=form, book_id=book_id),
                              context_instance=RequestContext(request))

def book_del(request, book_id):
    return HttpResponse('delete book')

class ImpressionList(ListView):
    context_object_name='impressions'
    template_name='cms/impression_list.html'
    paginate_by = 2

    def get(self, request, *args, **kwargs):
        book = get_object_or_404(Book, pk=kwargs['book_id'])
        impressions = book.impressions.all().order_by('id')
        self.object_list = impressions

        context = self.get_context_data(object_list=self.object_list, book=book)    
        return self.render_to_response(context)

def impression_edit(request, book_id, impression_id=None):
    book = get_object_or_404(Book, pk=book_id)
    if impression_id:
        impression = get_object_or_404(Impression, pk=impression_id)
    else:
        impression = Impression()

    if request.method == 'POST':
        form = ImpressionForm(request.POST, instance=impression)
        if form.is_valid():
            impression = form.save(commit=False)
            impression.book = book
            impression.save()
            return redirect('cms:impression_list', book_id=book_id)
    else:
        form = ImpressionForm(instance=impression)

    return render_to_response('cms/impression_edit.html',
                              dict(form=form, book_id=book_id, impression_id=impression_id),
                              context_instance=RequestContext(request))

def impression_del(request, book_id, impression_id):
    impression = get_object_or_404(Impression, pk=impression_id)
    impression.delete()
    return redirect('cms:impression_list', book_id=book_id)