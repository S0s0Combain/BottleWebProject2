%rebase('layout.tpl', title='Error', year=year)
<div class="container-error">
    <div class="error-card">
        <div class="error-message">{{ error_message }}</div>
    </div>
    <a href="/articles" class="back-button">Back</a>
</div>
<style>
    .error-card {
        background-color: #ffebee;
        border: 1px solid #f5c6cb;
        border-radius: 5px;
        padding: 20px;
        text-align: center;
        max-width: 600px;
        margin: 0 auto;
        width:600px;
    }
    .error-message {
        font-size: 24px;
        color: #c53030;
        margin-bottom: 20px;
    }
    .container-error {
        height: 65vh;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
    }
    .back-button {
        display: inline-block;
        background-color: #000;
        color: #fff;
        padding: 10px 20px;
        text-decoration: none;
        border-radius: 5px;
        transition: background-color 0.3s;
        margin-top: 20px;
    }
    .back-button:hover {
        background-color: #333;
    }
</style>
