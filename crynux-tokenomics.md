# Crynux Tokenomics

The CNX token serves as the utility token within the Crynux Network, facilitating the exchange of computational power. This role will expand in the future to include models and datasets. Applications use CNX to pay for AI tasks, while nodes earn CNX by executing them.

Beyond its use in paying for AI computation tasks, the CNX token is also integral to the governance of the DAO, including the election of the DAO Committee. This system ensures that Crynux remains a fully democratic, open, and community-governed organization, fostering its sustainable development in the long run.

The CNX token has a total supply of `CNX 8,617,333,262`. Which is the first 10 digits of the Boltzmann constant.

The CNX token is introduced through a fair launch. All tokens will be generated over a 21-year period in the form of node mining rewards. The majority of these tokens will be awarded to the node miners, while a smaller portion will be allocated to the DAO to support community development initiatives, such as application grants, and to cover development and marketing expenses.

## Token Emissions

In the initial phase of the project, the number of applications and nodes in the network is expected to be low. The growth of applications depends on the availability of sufficient computing power from the nodes. Therefore, node mining rewards will be higher in the early stages to incentivize more nodes to join the network.

As the network grows and the number of applications increases, the income for node miners will gradually shift from token emission incentives to the task fees earned from executing AI tasks.

Token emissions are scheduled over 21 years (Year 0 through Year 20), beginning with the testnet launch on January 1, 2024; Year 0 spans the entire testnet period until mainnet, after which Year 1 begins. Emissions decrease to 80% of the prior year's amount each year and cease after Year 20 when the total supply is reached.


```mermaid
xychart
  title "Token Emission Schedule"
  x-axis "Year" [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
  y-axis "Total Percentage (%)" 0 --> 100
  line [20.1862, 36.3351, 49.2543, 59.5896, 67.8579, 74.4725, 79.7642, 83.9975, 87.3842, 90.0935, 92.2610, 93.9950, 95.3822, 96.4919, 97.3797, 98.0900, 98.6582, 99.1127, 99.4764, 99.7673, 100.0000]
```


| Year | Percentage | Total Percentage | Emitted CNXs | Total CNXs |
| :--- | :--- | :--- | :--- | :--- |
| 0 | 20.1862% | 20.1862% | 1,739,510,807.74 | 1,739,510,807.74 |
| 1 | 16.1489% | 36.3351% | 1,391,608,646.19 | 3,131,119,453.94 |
| 2 | 12.9192% | 49.2543% | 1,113,286,916.95 | 4,244,406,370.89 |
| 3 | 10.3353% | 59.5896% | 890,629,533.56 | 5,135,035,904.45 |
| 4 | 8.2683% | 67.8579% | 712,503,626.85 | 5,847,539,531.31 |
| 5 | 6.6146% | 74.4725% | 570,002,901.48 | 6,417,542,432.79 |
| 6 | 5.2917% | 79.7642% | 456,002,321.18 | 6,873,544,753.97 |
| 7 | 4.2333% | 83.9975% | 364,801,856.95 | 7,238,346,610.92 |
| 8 | 3.3867% | 87.3842% | 291,841,485.56 | 7,530,188,096.48 |
| 9 | 2.7093% | 90.0935% | 233,473,188.45 | 7,763,661,284.92 |
| 10 | 2.1675% | 92.2610% | 186,778,550.76 | 7,950,439,835.68 |
| 11 | 1.7340% | 93.9950% | 149,422,840.61 | 8,099,862,676.29 |
| 12 | 1.3872% | 95.3822% | 119,538,272.48 | 8,219,400,948.77 |
| 13 | 1.1097% | 96.4919% | 95,630,617.99 | 8,315,031,566.76 |
| 14 | 0.8878% | 97.3797% | 76,504,494.39 | 8,391,536,061.15 |
| 15 | 0.7102% | 98.0900% | 61,203,595.51 | 8,452,739,656.66 |
| 16 | 0.5682% | 98.6582% | 48,962,876.41 | 8,501,702,533.07 |
| 17 | 0.4546% | 99.1127% | 39,170,301.13 | 8,540,872,834.20 |
| 18 | 0.3636% | 99.4764% | 31,336,240.90 | 8,572,209,075.10 |
| 19 | 0.2909% | 99.7673% | 25,068,992.72 | 8,597,278,067.82 |
| 20 | 0.2327% | 100.0000% | 20,055,194.18 | 8,617,333,262.00 |
| **Total** | **100.0000%** | | **8,617,333,262.00** | |

Tokens are emitted and distributed on a weekly basis. The number of tokens generated each week is based on the annual figures in the table above, and they are distributed according to the rules outlined below.

## Distribution of Token Emissions

### Year 0 and Year 1 Emission

| Item | Percentage    |
| ---- | --------------|
| Nodes         | 70%  |
| Treasury      | 30%  |
| Total         | 100% |

The first 2 year emissions will be distributed to the nodes, and the treasury. From the treasury's allocation, 35% is designated for early Crynux developers, while the remaining 65% is reserved for future DAO operations.

### Year 2-20 Emissions

|       Item     | Percentage |
| -------------- | ---------- |
| Nodes          | 80%        |
| Treasury       | 20%        |
| Total          | 100%       |

For the emission distribution from Year 2 to Year 20, 80% of the tokens are allocated to the nodes, and the remaining 20% to the treasury.

This structure is designed to heavily reward the nodes for providing the network's computational power, while also supporting the ecosystem's long-term growth through the DAO.

## Node Emission Calculation

The distribution of node emissions is directly tied to a node's contribution to the network, which is measured by the total task fees it earns during each weekly emission period. A node's share of the weekly emission pool is proportional to the amount of task fees it has collected relative to the total task fees collected by all nodes in the network.

For example, if a node earns 1% of the total task fees paid by applications across the network in a week, it will receive 1% of the total node emissions for that week.

This approach provides a simple yet effective mechanism for rewarding nodes fairly. The task fee a node earns is an organic reflection of its value to the network. A node's probability of being selected for tasks is determined by the performance (measured by the QoS score) and staking amount. Therefore, by pegging emissions to task fees, the system naturally rewards nodes that are both high-performing and contributed to the network's security. This creates a powerful incentive for all operators to maintain and improve their infrastructure, aligning individual node rewards with the overall health and efficiency of the network.
