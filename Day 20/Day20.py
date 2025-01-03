import logging
from collections import defaultdict

logging.basicConfig(
    level=logging.INFO,  # Set the logging level
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",  # Format for log messages
)


def get_factors(num: int) -> set[int]:
    """Gets the factors for a given number. Returns set[int] of factors.
    E.g. when num=8 factors will be 1, 2, 4, 8"""
    factors = set()

    for i in range(1, int(num**0.5) + 1):
        if num % i == 0:
            factors.add(i)
            factors.add(num // i)
    # logging.debug(factors)
    return factors


if __name__ == "__main__":
    ## Part 1
    TARGET = 33_100_000
    presents_dropped, house_num = 0, 0
    while presents_dropped < TARGET:
        house_num += 1
        presents_dropped = sum(factor * 10 for factor in get_factors(house_num))
        logging.debug("House=%d, presents dropped=%d", house_num, presents_dropped)
    logging.info(f"{house_num=}")
    ## Part 2
    presents_dropped, house_num = 0, 0
    elf_count = defaultdict(int)
    while presents_dropped < TARGET:
        presents_dropped = 0
        house_num += 1
        factors = get_factors(house_num)
        for elf in factors:
            count = elf_count[elf]
            if count < 50:
                elf_count[elf] += 1
                presents_dropped += elf * 11

    logging.info(f"{house_num=}")
