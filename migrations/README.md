# Migrations

This folder stores Flask-Migrate migration files.

If migrations are required, run:

```bash
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
```

This project currently uses:

```python
db.create_all()
```