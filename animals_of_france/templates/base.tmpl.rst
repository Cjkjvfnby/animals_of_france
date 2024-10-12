.. list-table::
   :class: field-list
   :widths: 1 1 1
{% for row in rows %}
{% for animal in row %}
   {% if loop.index0 == 0 %}*{% else%} {% endif %}{% if animal %} - .. figure:: {{animal.images[0].url}}
   {% else %} -{%endif%}{% endfor -%}

{% for animal in row %}
   {% if loop.index0 == 0 %}*{% else%} {% endif %}{% if animal %} - :doc:`/generated/{{animal.id -}}`{% else %} -{%endif%}{% endfor -%}
{% endfor -%}
