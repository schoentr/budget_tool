# Make a forms.py file

from django.forms import ModelForm
from .models import Card, Category

class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description']

class CardForm(ModelForm):
        class Meta:
            model = Card
            fields = ['']


# Create  CreateView in views.py

## Check out CCBV.CO.UK

from .forms import CategoryForm

class CategoryCreateView(loginRequiredMixin, CreateView):
    template_name = ' board/category_create.html'
    model = Category
    form_class = CategoryForm
    success_url = reverse_lazy('category_view')
    login_url = reverse_lazy('login')

    def form_valid(self,form):
        """Validate From Data"""
        form.instance.user = self.request.user
        return super().form_valid(form)


