from datetime import datetime


class LogMixin:
    @staticmethod
    def write(msg):
        with open('log.log', 'a+') as f:
            f.write(msg)
            f.write('\n')

    def log_info(self, msg):
        time = datetime.now()
        self.write(f'INFO: {msg} {time}')

    def log_error(self, msg):
        time = datetime.now()
        self.write(f'ERROR: {msg} {time}')
