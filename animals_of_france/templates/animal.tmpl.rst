{{animal.title}}
{{'=' * animal.title|length}}

- Français: {{animal.fr}}
- English: {{animal.en}}
- Русский: {{animal.ru}}
{% for image in animal.images %}
.. image:: {{image.url}}
   :target: {{image.url}}

{% if image.foto_date %}Was taken at {{image.foto_date}}{% endif %}
{% if image.coords %}`Was taken around this place <https://www.google.com/maps/search/?api=1&query={{image.coords}}>`__
{% endif -%}
{% endfor -%}
