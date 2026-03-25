# Isaak Liptzin Website

A minimal portfolio website built with Flask and HTML/CSS.

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the development server:
```bash
python3 app.py
```

## Adding Projects

Edit the `PROJECTS` list in `app.py`. You'll need Vimeo video IDs:

```python
{
    "id": "unique-id",
    "title": "Project Title",
    "vimeo_id": "123456789",  # Get from vimeo.com URL
    "description": "Project description"
}
```

## Customizing

- **Site title & name**: Edit `templates/base.html`
- **Colors & fonts**: Edit `static/style.css`
- **Social links**: Update footer links in `templates/base.html`
- **Email**: Update mailto link with your email




