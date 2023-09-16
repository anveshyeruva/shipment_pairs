# FIELDS: ORIGIN, DESTINATION, QUANTITY
SHIPMENTS = [
    ['US', 'US', 8],
    ['US', 'IN', 14],
    ['US', 'CA', 4],
    ['US', 'MX', 7],
    ['US', 'VE', 13],
    ['IN', 'US', 3],
    ['IN', 'IN', 13],
    ['IN', 'CA', 18],
    ['IN', 'MX', 16],
    ['IN', 'VE', 3],
    ['CA', 'US', 8],
    ['CA', 'IN', 20],
    ['CA', 'CA', 16],
    ['CA', 'MX', 3],
    ['CA', 'VE', 2],
    ['MX', 'US', 12],
    ['MX', 'IN', 20],
    ['MX', 'CA', 3],
    ['MX', 'MX', 3],
    ['MX', 'VE', 8],
    ['VE', 'US', 3],
    ['VE', 'IN', 7],
    ['VE', 'CA', 5],
    ['VE', 'MX', 15],
    ['VE', 'VE', 13],
 ]


def remove_intra(shipments):
    """remove_intra removes any records in which the origin and destination are the
    same country.
    """

    export_only = []
    for shipment in shipments:
        if shipment[0] != shipment[1]:
            export_only.append(shipment)
    return export_only


def collect_pairs(shipments):
    """collect_pairs collects shipments for each unique country pair on one row.
    Note: the entire data set should be sorted on shipment count--largest first.

    The resulting fields (since origin and destinations are on the same row) will
    be:
        COUNTRY_A, COUNTRY_B, QUANTITY_AB, QUANTITY_BA

    Example:
    >>> shipments = [
         ['US', 'IN', 14],
         ['US', 'CA', 17],
         ['IN', 'US', 8],
         ['IN', 'CA', 12],
         ['CA', 'US', 7],
         ['CA', 'IN', 5],
     ]
    >>> collect_pairs(shipments)
    [
        ['US', 'CA', 17, 7],
        ['US', 'IN', 14, 8],
        ['IN', 'CA', 12, 5],
    ]
    """

    shipment_pairs = []
    shipments = sorted(shipments, key=lambda x: x[2], reverse=True)

    for i in range(len(shipments) - 1):
        current_shipment = shipments[i]
        next_shipment = shipments[i + 1]
        if current_shipment[0] == next_shipment[0]:
            # same origin, so just add the quantities
            shipment_pairs.append(
                [current_shipment[0], current_shipment[1], current_shipment[2] + next_shipment[2], next_shipment[2]])
        else:
            # different origins, so create a new pair
            shipment_pairs.append([current_shipment[0], current_shipment[1], current_shipment[2], 0])
            shipment_pairs.append([next_shipment[0], next_shipment[1], 0, next_shipment[2]])

    return shipment_pairs


if __name__ == '__main__':

    # Part 1
    export_only = remove_intra(SHIPMENTS)
    print('#' * 80, ' ' * 30 + 'Intra Removed', '#' * 80, sep='\n')
    print(export_only)

    # Part 2
    shipment_pairs = collect_pairs(SHIPMENTS)
    print('\n', '#' * 80, ' ' * 30 + 'Pairs collected', '#' * 80, sep='\n')
    print(shipment_pairs)
