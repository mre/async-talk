import asyncio

boxes = 100 * [None]
BATCH_SIZE = 100

PACK_TIME = 0.001
TRANSPORT_TIME = 0.3


async def pack(boxes):
    print("Packing...")
    await asyncio.sleep(PACK_TIME)


async def transport(batch):
    print("Transporting...")
    await asyncio.sleep(TRANSPORT_TIME)


async def unpack(batch):
    print("Unpacking...")
    await asyncio.sleep(PACK_TIME)


def batches(items, size):
    for i in range(0, len(items), size):
        yield items[i : i + size]


async def move(batch):
    await pack(batch)
    await transport(batch)
    await unpack(batch)


async def main():
    all_batches = [move(batch) for batch in batches(boxes, 10)]
    await asyncio.gather(*all_batches)

asyncio.run(main())
