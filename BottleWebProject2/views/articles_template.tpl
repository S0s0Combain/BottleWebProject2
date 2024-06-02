%rebase('layout.tpl', title='Articles Page', year=year)

<div class="container-articles">
  <div class="sidebar">
    <h2>Add New Article</h2>
    <form action="/submit_article" method="post">
      <label for="author">Author Nickname:</label>
      <input type="text" id="author" name="author" required /><br />

      <label for="title">Title:</label>
      <input type="text" id="title" name="title" required /><br />

      <label for="description">Description:</label>
      <textarea id="description" name="description" required></textarea><br />

      <label for="date">Date (YYYY-MM-DD):</label>
      <input type="text" id="date" name="date" required /><br />

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
          <span class="author">{{ article["author"] }}</span>
          <h3>{{ article["title"] }}</h3>
          <p>{{ article["description"] }}</p>
          <div class="date">{{ article["date"]}}</div>
          <a href="{{ article["link"] }}" target="_blank">Read more</a>
        </li>
      % end
    </ul>
  </div>
</div>

<style>
  .container-articles {
    display: flex !important;
    width:100%!important!
    margin: 0 !important;
    justify-content: flex-start !important;
  }

  .sidebar {
    flex: 1 !important;
    border-right: 1px solid #ccc;
    background-color: #f4f4f4;
    padding: 20px;
  }

  .articles {
    flex: 4 !important;
    display: flex;
    flex-direction: column;
    align-items: center;
    width: 100%;
    justify-content: center;
  }

  h2 {
    text-align: center !important;
    color: #333 !important;
  }

  #articles-list {
    list-style-type: none !important;
    max-width: 800px;
    margin: 0 auto;
    flex-direction: column;
    padding: 0 !important;
  }

  #articles-list li {
    width:100%;
    background-color: #fff !important;
    margin: 20px 0 !important;
    padding: 30px 20px !important;
    border-radius: 10px !important;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1) !important;
    max-width: 800px;
  }

  #articles-list li .author {
    font-weight: bold !important;
  }

  #articles-list li .date {
    font-size: 0.9em !important;
    color: #777 !important;
  }

  form label {
    display: block !important;
    margin-bottom: 5px !important;
  }

  form input[type="text"],
  form textarea {
    width: calc(100% - 20px) !important;
    padding: 10px !important;
    margin-bottom: 10px !important;
    border: 1px solid #ccc !important;
    border-radius: 5px !important;
  }

  form button {
    display: block !important;
    width: 100% !important;
    padding: 10px !important;
    background-color: #333 !important;
    color: #fff !important;
    border: none !important;
    border-radius: 5px !important;
    cursor: pointer !important;
  }

  form button:hover {
    background-color: #555 !important;
  }
</style>