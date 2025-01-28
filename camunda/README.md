# Запуск:
Camunda:
```shell
cd camunda && docker compose -f camunda-platform/docker-compose.yaml up
```
Services:
```shell
cd camunda && docker compose up
```

# Для чего:
* Оркестрация инференсов.
* Оркестрация микросервисов на прмере `create_space`. Event sourcing.
* Оркестрация пользовательских бизнес процессов (`automl`, `active learning`, etc.)

# Results:
  * [-] В конце 2024 лицензия на ядро (zeebe) изменилась со свободной на платную. Всё остальное уже было платное для prod-а.
  * [?] BPMN-based: может быть как плюсом так и минусом.
  * [+] Отличный редактор BPMN (modeller). Может как чистые bpmn генерировать, так и с zeebe-расширением для camunda worker-ов.
  * [+] Есть контрольная панель (operate) для мониторинга и управления процессами.
  * [+] Есть business dashboard (optimize) для отслеживания KPI и поиска узких мест.
  * [+] Есть механизм миграций инстансов запущенных процессов из одной версии в другую.
