from client.infrastructure.settings.settings import Settings, LoggingType
from structured_logging.configuration.logger_config import LoggerConfig
from structured_logging.configuration.environment import Environment
from structured_logging.logger_creation.logger_config_builder import LoggerConfigBuilder
from structured_logging.processors.timestamp_processor import TimestampProccessor



def create_logger_config(settings: Settings, builder: LoggerConfigBuilder) -> LoggerConfig:
    if settings.logging_type == LoggingType.FILE:
        builder.with_file_sink(settings.logging_file_path)
    else:
        builder.with_console_sink()

    if settings.logging_is_async:
        builder.as_async(settings.logging_async_delay)

    environment = Environment(settings.environment.value)
    builder.add_environment(environment)
    builder.add_processor(TimestampProccessor())
    builder.add_masking(["card_number", "security_code"])

    return builder.build()