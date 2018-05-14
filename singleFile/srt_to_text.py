import re
import asyncio
import os

prog = re.compile(r"(^\d+:\d+:\d+,\d+ --> )")


async def convert_file(file_name):
    with open(file_name, 'r') as f:
        lines = f.readlines()
        lines[-1] += '\n'
    res = []
    try:
        for index, line in enumerate(lines):
            if prog.match(line):
                res.append(lines[index + 2])
                res.append(lines[index + 1])
                res.append('\n')
    except Exception as e:
        print(e)
        print(file_name)
        return
    with open(file_name.replace('srt', 'txt'), 'w') as f:
        f.writelines(res)


def main():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(
        asyncio.gather(
            *[convert_file(i) for i in os.listdir('.') if i.endswith('.srt')]))
    loop.close()


if __name__ == '__main__':
    main()
