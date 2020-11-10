# coding:utf-8
import logging


class LoggerMixin(object):
    def configure_file_logger(self):
        log_filename = self.config.get('LOG_FILENAME', None)

        if log_filename is not None:
            from logging.handlers import RotatingFileHandler

            # Create a file logger since we got a logdir
            file_handler = RotatingFileHandler(
                filename=log_filename,
                encoding='utf-8',
                maxBytes=1024 * 1024 * 8,
                backupCount=2)

            formatter = logging.Formatter(self.config['LOG_FORMAT'])
            file_handler.setFormatter(formatter)
            log_level = self.config.get('LOG_LEVEL', logging.WARNING)
            file_handler.setLevel(log_level)
            self.logger.addHandler(file_handler)
            self.logger.info("File logger started")
        else:
            self.logger.info("LOG_FILENAME not set. File logger skipped")

    def configure_email_logger(self):
        admins = self.config.get('ADMINS', None)

        if admins is not None:
            from logging.handlers import SMTPHandler

            admins_mail = map(lambda i: i[1], admins)
            from_email = self.config.get('FROM_EMAIL', 'webmaster@localhost')
            email_host = self.config.get('EMAIL_HOST', 'localhost')
            log_level = self.config.get('EMAIL_LOG_LEVEL', logging.ERROR)

            # as we have admins, mail logging to them
            email_handler = SMTPHandler(
                email_host,
                from_email,
                admins_mail,
                '%s Fail' % self.name.capitalize())

            email_handler.setLevel(log_level)
            self.logger.addHandler(email_handler)
            self.logger.info("Email logger started")
        else:
            self.logger.info("ADMINS not set. Email logger skipped")
