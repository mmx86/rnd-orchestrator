# Problem: Elasticsearch doesn't start with elasticsearch v7.
https://github.com/temporalio/docker-compose/issues/218

Fixed in elasticsearch v8.

Change env for quickfix.

```diff
diff --git a/.env b/.env
index 46fb9eb..b8ad1ff 100644
--- a/.env
+++ b/.env
@@ -1,6 +1,6 @@
 COMPOSE_PROJECT_NAME=temporal
 CASSANDRA_VERSION=3.11.9
-ELASTICSEARCH_VERSION=7.16.2
+ELASTICSEARCH_VERSION=8.16.0
 MYSQL_VERSION=8
 TEMPORAL_VERSION=1.26.2
 TEMPORAL_ADMINTOOLS_VERSION=1.26.2
(END)ngular2html

```

# Links
## Saga
* https://pages.temporal.io/rs/250-WIU-007/images/tech-guide-saga-pattern-made-easy.pdf
* https://temporal.io/blog/saga-pattern-made-easy
## Other
* https://www.youtube.com/watch?v=6T6zVZHU7_Q

