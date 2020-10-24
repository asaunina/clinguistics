# clinguistics
## Комментарий к программе 14(создание словаря)
**_Задание_**. На вход программе дается два слова: _русское_ и _английское_. Необходимо создать словарь, в который будут заноситься данные значения.

**Важно учитывать**, что нам не гарантировано, что пользователь введет слово, состоящее только из символов _кириллицы_ или _латиницы_, он также может вводить цифры, перемешивать символы. Поэтому необходимо сделать так называемую _проверку от дурака_.:eyes:

Что надо сделать, чтобы выполнить _проверку от дурака_:
1. Проверить, есть  в введенном значении цифры;
2. Проверить, содержатся в слове кроме букв от A до Z(a - z) буквы от А до Я(а - я) или наоборот: если кроме букв от А до Я(а - я) в значении содеражатся буквы от A до Z(a - z);
3. Если значение не соответствует условиям, вывести _Wrong answer_.

Вот пример ввода и вывода данных моей программы:
| 1 слово  | 2 слово  | Вывод                                             |
| ---------| :-------:| :-------------------------------------------------|
| h8llo    | goodbye  | wrong answer                                      |
| hello    | g88dbye  | wrong answer                                      |
| hello    | привет   | Русское слово - привет; The English word is hello |
| helлоу   | приvet   | wrong answer                                      |
  
Код можно найти по этой [ссылке](https://github.com/asaunina/clinguistics/commit/2a223af4d5eaa9ba54394957deb8d8af4022d8ba) :point_right::point_left:

Хорошего настроения! 

![Хорошего настроения!](https://sun9-26.userapi.com/c855028/v855028059/9a934/ZKeZ9Rua94E.jpg)

## Комментарий к заданию про Киркегора
_Регулярное выражение_ - К(ир|ьер|ер).*?(аард|ор)(а|ом|у)?

## Комментарий к заданию про tf-idf
**_TF_** (Term frequency)  — это частотность термина, которая измеряет, _насколько часто термин встречается в документе_. Логично предположить, что в длинных документах термин может встретиться в больших количествах, чем в коротких, поэтому абсолютные числа тут не катят. Поэтому применяют относительные — делят количество раз, когда нужный термин встретился в тексте, на общее количество слов в тексте.

То есть:

**_TF термина а = (Количество раз, когда термин а встретился в тексте / количество всех слов в тексте)_**

**_IDF_** (Inverse document frequency) — это обратная частотность документов. Она измеряет непосредственно _важность термина_. То есть, когда мы считали TF, все термины считаются как бы равными по важности друг другу. Но всем известно, что, например, предлоги встречаются очень часто, хотя практически не влияют на смысл текста. И что с этим поделать? Ответ прост — посчитать IDF. Он считается как логарифм от общего количества документов, делённого на количество документов, в которых встречается термин а.

То есть:

**_IDF термина а = логарифм(Общее количество документов / Количество документов, в которых встречается термин а)_**

P.S. Я не уверена, что у меня сделано это задание правильно, потому что мой код для tf выводит какие-то невероятные чиселки от 0.0003278 до 8.29382138(самые популярные и частоупотребляемые слова, как мне кажется, имеют нормальные значение, а остальные уже больше единички). Такое вообще возможно? :worried: А в idf у меня иногда получаются нормальные значения, иногда программа в конце выдает 0.0, а иногда вообще ошибку - division by zero... Не подскажете, как можно было бы улучшить программу? :innocent:

