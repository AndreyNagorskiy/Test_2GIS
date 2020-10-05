# **Тестовое задание 2GIS на позицию junior python developer**
<br>
Необходимо написать программу на Python, которая вычисляет общее время пребывания всех людей за каждое число.
<br>
Примечания: <br>
<ul>
  <li>Сделать реализацию, потребление памяти которой не зависит от размера входного файла;</li>
  <li>Сделать возможность разбивки по работникам и фильтрации по интервалам дат (например, с 01-08-2020 по 31-08-2020);</li>
  <li>Можно использовать любой фреймворк;</li>
  <li>Продемонстрировать работу с помощью тестов;</li>
  <li>Обеспечить максимально простое развёртывание приложения (например docker-контейнер);</li>
  <li>Исходный код выложить на github или bitbucket.</li>
 </ul>
 <h2>Тестирование</h2>
Для мониторинга использования памяти применял модуль Memory Profiler. Чтобы получить результаты тестов в консоли, необходимо расскоментировать декоратор @profile.
<h3>Результаты тестов</h3>
<ul>
<li>small_memory_test.xml - 600 байт<br><br><img src="https://sun4-16.userapi.com/bYzaIxQEtVgRokmeEl2Va95ro8AtjRJ3GJTjXA/JJreBPaSmDo.jpg"><br><br></li>
<li>middle_memory_test.xml - 148 КБ<br><br><img src="https://sun4-10.userapi.com/Ha5Ibv3LvzE4bew9vLbO_HnsI3E8MxpsVRBoXw/sdlIztLdTuk.jpg"><br><br></li>
<li>big_memory_test.xml - 4,05 МБ<br><br><img src="https://sun4-10.userapi.com/ovhPt7FwvETDi4QJ9-FTyYpw0WUISbX6nNYLWg/Dpatjrlb9l8.jpg"><br><br></li>
<li>very_big_memory_test.xml - 124 МБ<br><br><img src="https://sun4-12.userapi.com/XrC2M8bqMo1lj1wrAFR5kUNIpnH_RKn_72PPyA/Eca0SAzjzPI.jpg"><br><br></li> 
</ul>
<h2>Развертывание</h2>
Для развертывания приложения в Docker добавлен dockerfile на основе которого можно cобрать образ командой:<br> 
<i>docker build -t image_name .</i><br>
Затем запустить образ:<br>
<i>docker run -t -it image_name</i>
