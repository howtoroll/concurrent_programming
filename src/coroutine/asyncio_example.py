import sys
import asyncio


async def f1():
    print('Hello ...')
    await asyncio.sleep(1)
    print('... World!')


def main():
    if sys.version_info[0] < 3:
        return

    asyncio.run(f1())


if __name__ == "__main__":
    sys.exit(main())
