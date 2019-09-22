import time

boxes = 100 * [None]
BATCH_SIZE = 100

PACK_TIME = 0.02
TRANSPORT_TIME = 0.5


def pack(boxes):
    print("Packing...")
    time.sleep(BATCH_SIZE * PACK_TIME)
    batch, boxes[:] = boxes[:BATCH_SIZE], boxes[BATCH_SIZE:]
    return batch


def transport(batch):
    print("Transporting...")
    time.sleep(TRANSPORT_TIME)


def unpack(batch):
    print("Unpacking...")
    time.sleep(BATCH_SIZE * PACK_TIME)


def batches(items, size):
    for i in range(0, len(items), size):
        yield items[i : i + size]


def main():
    for batch in batches(boxes, 10):
        batch = pack(boxes)
        transport(batch)
        unpack(batch)


main()
