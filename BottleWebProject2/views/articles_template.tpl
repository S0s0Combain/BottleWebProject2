%rebase('layout.tpl', title='Articles Page', year=year)

<div class="container-articles">
  <div class="sidebar">
    <h2>Add New Article</h2>
    <form action="/submit_article" method="post">
      <label for="author">Author Nickname:</label>
      <input title="Latin characters and numbers" type="text" id="author" name="author" required /><br />

      <label for="title">Title:</label>
      <input title="Only Latin letters, numbers, spaces, and punctuation" type="text" id="title" name="title" required /><br />

      <label for="description">Description:</label>
      <textarea title="Only Latin letters, numbers, spaces, and punctuation" id="description" name="description" required></textarea><br />

      <label for="date">Date (YYYY-MM-DD):</label>
      <input title="Date should be in YYYY-MM-DD format." type="text" id="date" name="date" required /><br />

      <label for="link">Link:</label>
      <input type="text" id="link" name="link" required /><br />

      <button type="submit">Create</button>
    </form>
  </div>

  <div class="articles">
    <h2>Articles</h2>
    <ul id="articles-list">
        % for article in articles:
            <li>
                <h3><strong>{{ article["title"] }}</strong></h3>
                <p>{{ article["description"] }}</p>
                <div class="author-date">
                <span class="author"><strong>Author:</strong> {{ article["author"]}}</span>
                
                </div>
                <br/>
                <div class="date">{{ article["date"] }}</div>
                <a id="article-a" class="btn btn-primary" href="{{ article["link"] }}" target="_blank">Read more</a>
            </li>
        % end

    </ul>
  </div>
</div>