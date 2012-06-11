What & why
==========

What
----

This aims to rewrite the old, buggy, slow and unmaintained soup.io codebase.

Why
---

The current soup.io is implemented as a Ruby on Rails app. Unfortunately though it uses an quite old version of Ruby on Rails that has proven itself to be slow and unstable. Porting it to the current version of Ruby on Rails would equal to rewriting the whole thing, so that's what we're doing here (Although not with RoR anymore).

Technical foo
=============

From a technical standpoint, this is a Django project that uses South for schema migrations.

Dependencies
============

See `requirements.txt` for the dependencies of this. You can also use

	pip2 install -r requirements.txt

to automatically install them all.