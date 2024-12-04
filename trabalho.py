from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class FinanceApp(App):
    def build(self):
        self.title = "Calculadora de Rendimento"
        
        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # Campo para inserir o valor do investimento
        self.investment_input = TextInput(hint_text='Valor do Investimento', multiline=False, input_filter='float')
        self.layout.add_widget(self.investment_input)

        # Campo para inserir o número de meses
        self.months_input = TextInput(hint_text='Número de Meses', multiline=False, input_filter='int')
        self.layout.add_widget(self.months_input)

        # Botões para cada tipo de investimento
        self.cdi_button = Button(text='Investir em CDI (0,9% ao mês)')
        self.cdi_button.bind(on_press=self.calculate_cdi)
        self.layout.add_widget(self.cdi_button)

        self.ibovespa_button = Button(text='Investir em IBOVESPA (1,5% ao mês)')
        self.ibovespa_button.bind(on_press=self.calculate_ibovespa)
        self.layout.add_widget(self.ibovespa_button)

        self.br_button = Button(text='Investir em BR (0,7% ao mês)')
        self.br_button.bind(on_press=self.calculate_br)
        self.layout.add_widget(self.br_button)

        # Botão para resetar os campos
        self.reset_button = Button(text='Resetar Campos')
        self.reset_button.bind(on_press=self.reset_fields)
        self.layout.add_widget(self.reset_button)

        # Label para exibir o resultado
        self.result_label = Label(text='Rendimento: R$ 0,00')
        self.layout.add_widget(self.result_label)

        return self.layout

    def calculate_cdi(self, instance):
        self.calculate_rendimento(0.009)

    def calculate_ibovespa(self, instance):
        self.calculate_rendimento(0.015)

    def calculate_br(self, instance):
        self.calculate_rendimento(0.007)

    def calculate_rendimento(self, taxa):
        try:
            investimento = float(self.investment_input.text)
            meses = int(self.months_input.text)
            rendimento = investimento * ((1 + taxa) ** meses - 1)
            self.result_label.text = f'Rendimento: R$ {rendimento:.2f}'
        except ValueError:
            self.result_label.text = 'Por favor, insira valores válidos.'

    def reset_fields(self, instance):
        self.investment_input.text = ''
        self.months_input.text = ''
        self.result_label.text = 'Rendimento: R$ 0,00'

if __name__ == '_main_':
    FinanceApp().run()