from django import forms
from .models import Chamado

class ChamadoForm(forms.ModelForm):
    class Meta:
        model = Chamado
        fields = ['cliente', 'titulo', 'descricao', 'status', 'prioridade']
        widgets = {
            'cliente': forms.TextInput(attrs={'class': 'form-control'}),
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'status': forms.Select(attrs={'class': 'form-select'}),
            'prioridade': forms.CheckboxInput(attrs={'class': 'form-check-input'}), # Classe correta para Checkbox
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Vamos adicionar a classe em todos, EXCETO na prioridade
        for field_name, field in self.fields.items():
            if field_name != 'prioridade':
                field.widget.attrs.update({'class': 'form-control'})