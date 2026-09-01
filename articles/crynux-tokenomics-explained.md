# Crynux is changing how CNX gets paid out: tying emissions to real network growth

A new CNX tokenomics change was voted through by the Crynux DAO Council this week (<a href="https://crynux-network-dao.github.io/crynux-dao-webui/proposals/94212817319976146050097078557687113067264882051365253388963838063529756964910">proposal and vote record</a>) and is now officially in effect. It changes how CNX gets issued going forward, ties most of the remaining supply to real usage instead of time, and cuts the testnet allocation that was paying out regardless of demand. Here's the full mechanism, every number behind it, and how it stacks up against what's worked and failed elsewhere.

## At a glance

| | Before | Now |
| --- | --- | --- |
| Testnet / Year 0 | 20% of supply | 9% of supply |
| Bootstrap mining | Part of scheduled emissions | 20% of supply |
| Task mining | Part of scheduled emissions | 71% of supply |
| Scheduled Year 1 emissions | 13.26M CNX / week | \~1.79M CNX / week bootstrap (\~1.43M to nodes); task mining releases on usage only |
| What drives emissions? | Primarily time | Primarily real network usage |
| Total CNX supply | 8.617B | Unchanged: 8.617B |

## The problem with paying on a calendar

Under the previous model, CNX emissions ran on a fixed schedule. Tokens were issued on a clock, the same amount whether the network processed ten tasks that week or ten million. That created a timing problem: issuance was heaviest in the earliest years, exactly when real usage was lightest. The ratio of new supply to actual network activity was worst at the exact moment the market was forming its first opinion of the token. That wasn't a Crynux-specific flaw, it's structural to any schedule that pays for time passing instead of paying for work done.

There's a second-order cost too. When rewards accrue mainly for being online, a rational node operator optimizes for cheap uptime, not for being genuinely useful to developers. Tying the largest pool to completed task volume instead aligns operator incentives with what the network is actually for.

The obvious fix, "just emit less", isn't complete on its own. A compute network has a cold-start problem: capacity has to exist before demand arrives. If the first developers to try Crynux find slow or unavailable nodes, they don't come back, and real task volume never materializes to justify further emission. Cutting issuance to near zero and waiting for organic demand risks killing the network from the other direction. That's why this change doesn't just lower emission, it splits emission into two pools with two different jobs.

## What's changing: the two-pool split

After Year 0, node mining splits as follows.

**Bootstrap mining: 20% of total supply.** Calendar-based, released over Years 1 to 20 on a decay curve. Its only job is liveness: keeping enough GPUs online and staked before task fees alone can cover an operator's cost. The release follows an Avrami curve, the same math used to model crystal growth in materials science, and the actual origin of the project's name (crystallization + nucleation):

```text
F(y) = scale × (1 - exp(-k × y^n)) / (1 - exp(-k × 20^n))
```

scale = 0.20 (the bootstrap pool), k = 0.0538, n = 1.4, y = year index 1 to 20

In Year 1 this comes to roughly 1.79M CNX per week in total, of which about 1.43M goes to nodes. The weekly amount rises through the middle years before tapering off; the full year-by-year calendar is published in the DAO tokenomics document.

Each node's weekly share of bootstrap mining is proportional to the task fees it earned that week, including fees from heartbeat tasks (ordinary AI tasks the network dispatches on its own so the fee-based split still has something real to calculate against when few applications are sending traffic) plus any real application tasks. Example from the docs: a node earning 1% of total network task fees in a week receives 1% of that week's bootstrap release. A node's odds of being selected for tasks at all come down to its QoS (quality of service) score and staking amount, so higher stake and better performance both compound into a larger share.

**Task mining: 71% of total supply,** the majority of the entire allocation. This pool doesn't run on calendar time at all. It's released against "effective network time", a measure of real completed application tasks compared to a planned usage curve, similar in spirit to how Filecoin's baseline minting works. The full mechanism:

Target node count over time:

```text
N(a) = b0 × exp(g × a)
```

Network utilization ramping up:

```text
mu(a) = 1 - exp(-a × ln(2) / h)
```

Planned application tasks in month a, where t_hat is the estimated time to execute one task:

```text
K(a) = mu(a) × (86400 × 30 × N(a)) / t_hat
```

Cumulative planned tasks:

```text
K_cum(a) = sum of K(i) for i = 1 to a
```

Effective network time is the largest month a where the cumulative planned task count is still less than or equal to the actual cumulative completed tasks. The release itself follows the same Avrami shape as bootstrap mining, but stepped forward by that effective time instead of the calendar:

```text
F(t) = scale × (1 - exp(-k × (c1 × t + c0)^n))
```

scale = 0.71 (the task mining pool), t = effective network time

The task-mining framework is fixed. Its usage-milestone parameters (b0, g, h, t_hat, and the curve parameters k, n, c0 and c1) are set by DAO vote as real usage data comes in, and until they are set, nothing releases from this pool. Depending on how fast real usage grows, the pool may finish earlier or later than 20 years.

If effective network time doesn't advance by at least a full step, nothing releases from this pool that period. Low real usage means most of this pool is simply never issued, not burned, not redirected, just held unminted until demand actually justifies it. Each node's share of what does release is proportional to the application task fees it earned in that period, using only real application fees; heartbeat tasks don't count toward this pool the way they do for bootstrap mining.

**Year 0 / Testnet allocation:** cut from 20% to 9% of total supply (nodes from 14% to 3%; treasury unchanged at 6%). Of that treasury slice, 35% is earmarked for early Crynux developers and the remaining 65% is reserved for future DAO operations.

## The vesting details

This part matters and gets skipped a lot: how fast do these rewards actually become usable?

**Year 0 / testnet rewards:** unlocked testnet tokens are untouched. Each node's remaining locked balance at the testnet-end snapshot is converted pro-rata into the new 3% pool and continues on the original 12-month linear vesting schedule from mainnet launch, with daily distribution.

**Bootstrap mining and task mining rewards:** each release follows an 80% nodes / 20% treasury split, and the node portion vests over 6 months, linearly, distributed daily.

This change affected locked tokens only. Every CNX already unlocked, on mainnet and on testnet, stays exactly where it is.

On mainnet, the first months of mining under the old schedule had already paid out more in unlocked tokens than the same period would have paid in total, locked and unlocked combined, under the new schedule. The remaining locked balances were therefore removed and stay in the unminted supply. No mainnet miner ends up behind where the new schedule would have placed them. New bootstrap emissions begin a fresh six-month vesting period from the vote.

## Why the testnet cut, specifically

Helium, Crynux's testnet (January 1, 2024 to June 17, 2026), genuinely proved the network works: 1,785 active nodes, 55 million tasks completed, 230 million CNX paid to real operators. That track record is why mainnet (Lithium) could launch with a working system behind it instead of a whitepaper promise.

But that demand was protocol-subsidized, tasks the network paid for itself to prove the system functioned, not application usage from outside users with their own reasons to be there. That was the right design for proving a system. It's not a reason to keep allocating a fifth of all mining supply to a phase that's already served its purpose. Unlocked testnet tokens are untouched. Locked balances were scaled down with the allocation and continue on their original schedule.

## How this compares to other networks' emission bets

**What survived:**

**Bitcoin** pays for security on a pure calendar schedule with no usage gate at all, and it worked, but only because Bitcoin's product is the money. Demand scaled on a monetary narrative that doesn't need an on-chain usage metric. A network selling compute as a service doesn't get that shortcut.

**Monero** has run a tail emission under 1% a year since 2022, low, predictable, never large enough to overwhelm demand. It's the least exciting tokenomics story in crypto and one of the few that's never needed rescuing.

**Kaspa** front-loaded emission hard early and survived it because an exceptional narrative bid happened to arrive at the same time as the supply. It now runs a fraction of that original rate at a far larger network size; the low-emission state was always the sustainable one, the heavy phase was something to survive, not the reason it worked.

**What didn't:**

**Helium,** the IoT network (no relation to Crynux's own testnet phase of the same name), paid enormous emissions for hotspot deployment without ever gating issuance on whether anyone actually bought the coverage. Close to a million hotspots went up worldwide. Real paid data revenue stayed negligible, reportedly in the low thousands of dollars a month against emissions worth orders of magnitude more. The token drew down roughly 99% from its high and the tokenomics had to be rebuilt from scratch. The emission wasn't too large, it was attached to the wrong thing: capacity, not usage.

**Axie Infinity's SLP** and **STEPN's GST** both tied issuance to user activity, which sounds exactly like what Crynux is now proposing. Both discovered that when tokens are the reward for activity, the activity becomes a token-farming operation instead of genuine demand. Both collapsed.

| Project | What it pays for | Gated on real demand | Outcome |
| --- | --- | --- | --- |
| Bitcoin | Security, calendar schedule | No | Survived, product is the money |
| Monero | Security, tail emission &lt;1%/yr | No, but too small to matter | Survived, never overwhelmed demand |
| Kaspa | Security, front-loaded calendar | No | Survived on narrative bid; now runs low emission |
| Helium (IoT) | Hotspot capacity deployed | No | Collapsed, \~99% drawdown, rebuilt |
| Axie (SLP) / STEPN (GST) | User "activity" | Yes, but gameable | Collapsed, activity got farmed |
| Crynux | Verified compute tasks | Yes, sampled re-execution | In effect |

Tying emissions to usage introduces a different risk: if "usage" can be manufactured purely to earn tokens, the system can be farmed, the same problem that killed Axie and STEPN. Crynux's answer to that risk is its sampling validation: a random, undisclosed subset of tasks is re-executed and cross-checked, and nodes caught returning wrong results have staked CNX slashed. That verifies execution, that a task really ran and returned a correct result. It does not by itself verify that a task was wanted, so the release rules also have to make manufactured tasks unprofitable. That is the part most worth watching now that the task-mining pool is live.

## What this means, by group

**CNX holders:** the largest pool (71%) can't be issued ahead of real demand. New supply becomes evidence of usage, not just time passing.

**Testnet miners:** you're first in line for the 71% pool since you already have hardware and stake in place before application volume arrives, and that pool is far larger than anything the testnet allocation represented. The CNX you already hold from testnet also represents a larger share of the circulating supply trajectory under this change, as significantly fewer tokens are scheduled to enter circulation early.

**Node operators going forward:** bootstrap mining keeps running a node viable early; task mining ties long-term upside directly to completed, verified work instead of uptime alone.

**Builders:** capacity already exists when you arrive, because bootstrap mining pays for exactly that. Every application shipped grows the pool node operators are competing to serve, so adoption and available capacity start reinforcing each other.

## What stays exactly the same

- Total supply: 8,617,333,262 CNX (the first 10 digits of the Boltzmann constant), fixed.
- No pre-mine, no VC tranche, no founder allocation. Early developer compensation comes only from 35% of the Year 0 treasury allocation, about 2% of total supply, disclosed above.
- 80/20 split between node miners and the DAO treasury on every bootstrap / task mining release.
- Every CNX already unlocked, mainnet and testnet.

## One structural change, not an ongoing pattern

The emission structure adopted in this vote is final: total supply, the three allocations, the vesting schedules and the bootstrap curve are not planned to change. The only parameters still open by design are the task-mining usage milestones, which the DAO sets by vote as real usage data comes in, and any such vote is published before it takes effect. That is milestone-setting inside a fixed framework, not a tokenomics change.

Every project in that table made a bet at some point about what its emission was actually worth paying for. Bitcoin bet security would matter forever, and it was right. Helium bet nobody would check whether the coverage was real, and it was wrong. Axie and STEPN bet that "activity" was a safe enough thing to reward, and found out the hard way that anything you pay people to do eventually gets done for the payment instead of the reason you wanted it done.

Crynux is making a specific, checkable bet of its own: that verified compute demand, not uptime, not time elapsed, not a number that sounds like growth, is the one metric worth tying nearly three-quarters of its remaining supply to. It's willing to let that pool sit unminted for however long it takes for real usage to catch up, rather than pay it out on a schedule and hope demand eventually shows up to match.

That's a harder position to defend than "trust the roadmap."

Vote record: [https://crynux-network-dao.github.io/crynux-dao-webui/proposals/94212817319976146050097078557687113067264882051365253388963838063529756964910](https://crynux-network-dao.github.io/crynux-dao-webui/proposals/94212817319976146050097078557687113067264882051365253388963838063529756964910)

Full tokenomics specification: [https://github.com/crynux-network-dao/crynux-dao-documents/blob/main/crynux-tokenomics.md](https://github.com/crynux-network-dao/crynux-dao-documents/blob/main/crynux-tokenomics.md)
