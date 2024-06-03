%rebase('layout.tpl', title='Error', year=year)
<div class="container-error">
    <div class="error-card">
        <div class="error-message">{{ error_message }}</div>
    </div>
    <a href="/articles" class="back-button">Back</a>
</div>