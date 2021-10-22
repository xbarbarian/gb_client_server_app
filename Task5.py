# 5. Выполнить пинг веб-ресурсов yandex.ru, youtube.com
# и преобразовать результаты из байтовового в строковый тип на кириллице.
import subprocess

ping_remote_host = [['ping', 'yandex.ru'], ['ping', 'youtube.com']]


def decode_cp866(args):
    return args.decode('cp866')


def decode_utf8(args):
    return args.decode('utf-8')


for ping in ping_remote_host:
    ping_process = subprocess.Popen(ping, stdout=subprocess.PIPE)
    print(ping_process)

    i = 0
    for line in ping_process.stdout:
        if i < 5:
            # print(line)
            line = decode_cp866(line).encode('utf-8')
            print(decode_utf8(line))
            i += 1
        else:
            break
