from kivy.config import Config

width_of_screen = 600
height_of_screen = 600
# stats = {'Психика' : 100, 'Интеллект' : 100, 'Авторитетность' : 100}
index_of_random_words = 0

# Config.set('graphics', 'resizable', False)
# Config.set('graphics', 'width', width_of_screen)
# Config.set('graphics', 'height', height_of_screen)

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.codeinput import CodeInput
from pygments.lexers import HtmlLexer
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.scatter import Scatter
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label


class TestApp(App):
    def update_stats(self):
        self.Stats_Popular.text = f'Авторитетность\n{self.stats["Авторитетность"]}'
        self.Stats_Smart.text = f'Интеллект\n{self.stats["Интеллект"]}'
        self.Stats_Psycho.text = f'Психика\n{self.stats["Психика"]}'
        # if self.stats["Психика"] < 35:
        #     self.Stats_Psycho.background_color = [1, 0, 0, 1]
        # if self.stats["Интеллект"] < 35:
        #     self.Stats_Smart.background_color = [1, 0, 0, 1]
        # if self.stats["Авторитетность"] < 35:
        #     self.Stats_Popular.background_color = [1, 0, 0, 1]

    def build(self):
        self.stats = {'Психика': 100, 'Интеллект': 100, 'Авторитетность': 100}
        self.Stats_Psycho = Label(text=f'Психика\n{self.stats["Психика"]}',
                                  font_size=10, halign="center")
        self.Stats_Smart = Label(text=f'Интеллект\n{self.stats["Интеллект"]}',
                                 font_size=10, halign="center")
        self.Stats_Popular = Label(text=f'Авторитетность\n{self.stats["Авторитетность"]}',
                                   font_size=10, halign="center")
        Main_Grid = GridLayout(cols=3, padding=[50], spacing=3)
        Main_Grid.add_widget(self.Stats_Psycho)
        Main_Grid.add_widget(self.Stats_Smart)
        Main_Grid.add_widget(self.Stats_Popular)

        Main_Grid.add_widget(Button(text='Покушать в KFC',
                                    on_press=self.eat_in_KFC,
                                    font_size=10))
        Main_Grid.add_widget(Button(text='Поделать уроки',
                                    on_press=self.do_hw,
                                    font_size=10))
        Main_Grid.add_widget(Button(text='Кого-то унизить',
                                    on_press=self.scream_on,
                                    font_size=10))
        return Main_Grid

    def eat_in_KFC(self, instance):
        self.stats['Психика'] += 5
        self.stats['Интеллект'] -= 5
        self.update_stats()

    def do_hw(self, instance):
        self.stats['Интеллект'] += 5
        self.stats['Авторитетность'] -= 5
        self.update_stats()

    def scream_on(self, instance):
        self.stats['Авторитетность'] += 5
        self.stats['Психика'] -= 5
        self.update_stats()


# class MyApp(App):
#     def build(self):
#         s = Scatter()
#         fl = FloatLayout(size=(300, 300))
#         s.add_widget(fl)
#         fl.add_widget(Button(text='Попробуй',
#                              font_size=30,
#                              on_press=self.btn_press,
#                              background_color=[0, 1, 0, 1],
#                              background_normal='',
#                              size_hint=(0.5, 0.5),
#                              pos=(width_of_screen / 2 - (width_of_screen / 8), height_of_screen / 2 - (height_of_screen / 8))))
#         return s
#
#     def btn_press(self, instance):
#         global index_of_random_words
#         if index_of_random_words != 3:
#             instance.text = random_words[index_of_random_words]
#             instance.font_size = 20
#             index_of_random_words += 1
#         else:
#             instance.text = random_words[index_of_random_words]
#             instance.font_size = 20
#             index_of_random_words = 0


if __name__ == '__main__':
    TestApp().run()



