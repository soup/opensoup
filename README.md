Opensoup – What, why and how
============================

This aims to rewrite the old, buggy, slow and unmaintained soup.io codebase.

Why
---

The current soup.io is implemented as a Ruby on Rails app. Unfortunately though it uses an quite old version of Ruby on Rails that has proven itself to be slow and unstable. Porting it to the current version of Ruby on Rails would equal to rewriting the whole thing, so that's what we're doing here (Although not with RoR anymore).

How
---

Basically, the first goal is to build something that looks and feels as close to the current soup.io as possible, altough some not so commonly used features (TV?) should maybe be left out for the sake of simplification.

Communication
--------------

Current communication is via the IRC channel #soupdev on irc.libertirc.net. Maybe someone™ will some day set up a mailinglist.

Technical foo
-------------

From a technical standpoint, this is a Django project that uses South for schema migrations.

Testing locally
----------------

Run the following commands to  get opensoup running locally for the first time:

	# Install python dependencies
	pip2 install -r requirements.txt

	# Populate system tables
	python2 manage.py runserver

	# Run migrations
	python2 manage.py migrate

	# Collect staticfiles
	python2 manage.py collectstatic

	# Run the server
	python2 manage.py runserver
