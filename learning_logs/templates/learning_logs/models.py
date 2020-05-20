{% extends "learning_logs/base.html" %}

{% block page_header %}
  <h1>Topics.</h1>
{% endblock page_header %}

{% block content %}

  <ul>
  	{% for topic in topics %}
  	  <li><h3>
  	  	<a href="{% url 'learning_logs:topic' topic.id %}">{{ topic }}</a>
  	  </h3></li>
  	{% empty %}
  	  <li><h3>No topics have been added yet.</h3></li>
  	{% endfor %}
  </ul>

  <h3><a href="{% url 'learning_logs:new_topic' %}">Add a new topic</a></h3>
  
{% endblock content %}	