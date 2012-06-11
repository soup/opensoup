What & why
==========

This aims to rewrite the old, buggy, slow and unmaintained soup.io codebase. The first goal is to make it look & feel as close to the current soup.io as possible, altough some not so commonly used features should maybe be left out (TV?).

Why
---

The current soup.io is implemented as a Ruby on Rails app. Unfortunately though it uses an quite old version of Ruby on Rails that has proven itself to be slow and unstable. Porting it to the current version of Ruby on Rails would equal to rewriting the whole thing, so that's what we're doing here (Although not with RoR anymore).

Communication
=============

Current communication is via the IRC channel #soupdev on irc.libertirc.net. Maybe someone™ will some day set up a mailinglist.

Technical foo
=============

From a technical standpoint, this is a Django project that uses South for schema migrations.

Dependencies
============

See `requirements.txt` for the dependencies of this. You can also use

	pip2 install -r requirements.txt

to automatically install them all.