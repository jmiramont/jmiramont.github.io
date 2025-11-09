---
layout: default
title: Publications
permalink: /publications/
# title: List of Publications
---

<h2>Preprints</h2>
<ol>
  {% assign pubs = site.data.publications | where_exp: "item", "item.journal contains 'preprint'" %}
  {% assign sorted_pubs = pubs | sort: "pub_year" | reverse | slice: 0, 5 %}
  {% for publication in sorted_pubs%}
    <li>
      {% if publication.author %}<span>{{ publication.author }}</span>.<br>{% endif %}
      {% if publication.title %}<strong>{{ publication.title }}</strong>.<br>{% endif %}
      {% if publication.journal %}<em>{{ publication.journal }}</em>{% endif %}
      {% if publication.pub_year %}{% if publication.journal %}, {% endif %}{{ publication.pub_year }}.{% endif %}
    </li>
  {% endfor %}
</ol>

<h2>Publications</h2>
<ol>
  {% assign pubs = site.data.publications%}
  {% assign sorted_pubs = pubs | sort: "pub_year" | reverse %}
  {% for publication in sorted_pubs %}
      {% unless publication.journal contains 'preprint'%}
    <li>
      {% if publication.author %}<span>{{ publication.author }}</span>.<br>{% endif %}
      {% if publication.title %}<strong>{{ publication.title }}</strong>.<br>{% endif %}
      {% if publication.journal %}<em>{{ publication.journal }}</em>{% endif %}
      {% if publication.pub_year %}{% if publication.journal %}, {% endif %}{{ publication.pub_year }}.{% endif %}
    </li>
      {% endunless %}
  {% endfor %}
</ol>