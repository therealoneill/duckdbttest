from flask import Flask, render_template_string, request

app = Flask(__name__)

# HTML template string
HTML_TEMPLATE = """
<!doctype html>
<html>
<head><title>Flask WebApp Example</title></head>
<body>
  <h1>Flask WebApp Example with Form Elements</h1>
  <form method="post">
    <label for="entry">This is a label:</label>
    <input type="text" id="entry" name="entry"><br><br>

    <input type="submit" value="Submit"><br><br>

    <textarea name="text" rows="4" cols="50">This is a text area</textarea><br><br>

    <input type="checkbox" id="checkbox" name="checkbox" value="checked">
    <label for="checkbox"> Check me</label><br><br>

    <input type="radio" id="option1" name="radio" value="option1">
    <label for="option1">Option 1</label><br>
    <input type="radio" id="option2" name="radio" value="option2">
    <label for="option2">Option 2</label><br><br>

    <label for="dropdown">Choose an option:</label>
    <select id="dropdown" name="dropdown">
      <option value="option1">Option 1</option>
      <option value="option2">Option 2</option>
      <option value="option3">Option 3</option>
    </select><br><br>

    <label for="listbox">A listbox (use Ctrl to select multiple):</label>
    <select id="listbox" name="listbox" multiple>
      <option value="item1">Item 1</option>
      <option value="item2">Item 2</option>
      <option value="item3">Item 3</option>
    </select><br><br>
  </form>

  {% if submitted %}
  <h2>Form Data Submitted</h2>
  <p>Entry: {{ entry }}</p>
  <p>Text Area: {{ text }}</p>
  <p>Checkbox: {{ checkbox }}</p>
  <p>Radio: {{ radio }}</p>
  <p>Dropdown: {{ dropdown }}</p>
  <p>Listbox: {{ listbox }}</p>
  {% endif %}
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        # Process the form data
        submitted_data = {
            'submitted': True,
            'entry': request.form.get('entry'),
            'text': request.form.get('text'),
            'checkbox': request.form.get('checkbox', 'Not checked'),
            'radio': request.form.get('radio', 'None selected'),
            'dropdown': request.form.get('dropdown'),
            'listbox': request.form.getlist('listbox')  # For multiple selections
        }
        return render_template_string(HTML_TEMPLATE, **submitted_data)
    return render_template_string(HTML_TEMPLATE, submitted=False)

if __name__ == '__main__':
    app.run(debug=True)
