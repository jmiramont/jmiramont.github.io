---
layout: default
title: Publications
permalink: /publications/
title: List of Publications
---

<h2>List of Publications</h2>
<ol>
  {% assign sorted_publications = site.data.publications | sort: "year" | reverse %}
  {% for publication in sorted_publications %}
    <li>
      <strong>{{ publication.title }}</strong> ({{ publication.year }}) - 
      <a href="{{ publication.link }}" target="_blank">Read Article</a>
    </li>
  {% endfor %}
</ol>