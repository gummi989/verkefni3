<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
<div class="row">
    <section><h3>{{ frettir[0][0]}}</h3></section>
    <section><img src='/static/mynd0.jpg'></section>
    <section>
        <ul>
            % cnt = 0;
            % for i in frettir:
                <li><a href="/frett/{{cnt}}">{{i[0]}}</a></li>
                % cnt += 1
            % end
        </ul>
    </section>
<div>
    <h1> {{ fyrirsogn }} </h1>
    <p> {{ frett }} </p>
	<img src='./public/img/{{ mynd }}'>
	<p> höfundur, {{ hofundur }} </p>
</div>
</body>
</html>
