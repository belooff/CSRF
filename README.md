# Cross-Site Request Forgery

Practical examples of CSRF.

Есть веб-сервис со следующими точками входа:  

* GET / - перенаправляет пользователя на страницу /account
* GET /account - возвращает страницу, на которой отображено текущее состояние аккаунта пользователя и форма для перевода денег на чужой счет. На этой странице также устанавливаются cookie пользователя;  
* POST /withdraw - эндпоинт для перевода денег на чужой счет. После перевода возвращает пользователя на страницу /account;  
* GET /danger - мошенническая страница, эксплуатирующая уязвимость сайта к CSRF-атаке. При загрузке страницы будет отправлен AJAX-запрос на /withdraw, а после выполнения запроса произойдет перенаправление на страницу /account.

Вам дан пользователь user1 с паролем password и начальным счетом. При отправке формы на странице /account происходит списание 1 единицы со счета. Кроме того, переход на страницу /danger также неявно приводит к списанию со счета, если были установлены cookies (т.е. если пользователь ранее посещал /accounts).

Требуется, не меняя логику работы вредоносного скрипта /danger, изменить логику работы /withdraw и /account таким образом, чтобы переход на страницу /danger не приводил к списанию денег со счета пользователя. Для этого необходимо добавить cookie, недоступный /danger, в тело запроса.

Обратите внимание, что ситуация, приведенная в задаче, является лишь практическим упражнением для разработки защиты от CSRF. В данном примере зловредный скрипт /danger находится на одном домене с /withdraw и имеет возможность получить cookie. В реальных случаях зловредный скрипт обычно располагается на чужом домене. Политика современных браузеров запрещает получать cookie с других доменов (т.н. third-party cookie). Тем не менее если злоумышленник имеет возможность вставить зловредный скрипт на страницу вашего домена (например, при помощи XSS), то защита от CSRF будет бесполезна.
