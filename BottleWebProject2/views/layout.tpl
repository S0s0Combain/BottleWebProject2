<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ title }} - My Bottle Application</title>
    <link rel="stylesheet" type="text/css" href="/static/content/bootstrap.min.css" />
    <link rel="stylesheet" type="text/css" href="/static/content/site.css" />
    <link rel="stylesheet" type="text/css" href="/static/content/about_us_style.css"/>
    <link
      rel="stylesheet"
      type="text/css"
      href="static/content/catalog.css"
    />
            <link rel="stylesheet" type="text/css" href="/static/content/main_page_style.css" />
            <link
        rel="stylesheet"
        href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css"
    />
</head>

<body>
    <div class="navbar navbar-inverse navbar-fixed-top">
        <div class="container">
            <div class="navbar-header">
                <button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-collapse">
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                </button>
                <a href="/" class="navbar-brand" id="brand-name-header">AnForce</a>
            </div>
            <div class="navbar-collapse collapse">
                <ul class="nav navbar-nav">
                    <li><a href="/catalog">Catalog</a></li>
                    <li><a href="/about_us">About Us</a></li>
                    <li><a href="/articles">Articles</a></li>
                    <li><a href="/reviews">Reviews</a></li>
                </ul>
            </div>
        </div>
    </div>
    {{!base}}
    <footer>
        <div class="container-links">
            <a href="https://www.instagram.com/ralphlauren/" target="_blank"><i class="fab fa-instagram" title="Go to Instagram brand"></i></a>
            <a href="https://www.pinterest.com/ralphlauren/" target="_blank"><i class="fab fa-pinterest" title="Go to Telegram brand"></i></a>
            <a href="https://www.facebook.com/RalphLauren/" target="_blank"><i class="fab fa-facebook" title="Go to Facebook brand"></i></a>
            <a href="https://www.youtube.com/user/RLTVralphlauren" target="_blank"><i class="fab fa-youtube" title="Go to YouTube brand"></i></a>
        </div>
    </footer>

        <script src="/static/scripts/modernizr-2.6.2.js"></script>
    <script src="/static/scripts/jquery-1.10.2.js"></script>
    <script src="/static/scripts/bootstrap.js"></script>
    <script src="/static/scripts/respond.js"></script>

</body>
</html>
