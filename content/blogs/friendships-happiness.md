Title: On Happiness and Explore-Exploit Algorithms
Date: 2022-11-23
Modified: 2022-11-23 10:15 PM
Category: IRL
Tags: philosophy, cs
Status: draft
Slug: friendships-happiness
Summary: I pontificate about friendships, happiness, and greedy algorithms.

## 1. Introduction to the Explore/Exploit paradigm

In an episode of one of CGP Grey's podcasts (I unfortunately can't remember which one), I was first introduced to the concept of explore-exploit algorithms.

The setup for these is pretty basic. I like to imagine it as a robot being teleported into this infinite 2D plane. Randomly scattered on the plane are different resources which — crucially — have different values. Each of these resources can be mined infinitely, with the value solely deciding how fast the robot gains points from mining that resource. The also robot knows nothing about the relative frequencies of the resources and the values of resources cannot be ascertained until it has mined them for a non-neglible amount of time.

![Robot on 2D plane]({static}/images/friendships-happiness/robot.png)

The question is, given a time constraint, *what should the robot do to optimize its points by the end of the time?* This is a question with a pretty intuitive answer, and I'd recommend that the inquisitive reader spends thirty seconds or so pondering it.

(The next sentence is a spoiler).

The answer is to first explore for *m* steps of time and then exploit for the remaining *n* steps of time. The exact proportions of *m* and *n* depend on the specifics of the resource distribution and value distribution. But the core idea remains the same: explore first, exploit later.

I feel that the logic to prove this answer is fairly elegant, so I'll quote the relevant section from Langford et al.'s "Competitive Analysis of the Explore/Exploit Tradeoff," a paper written by some researchers from the University of Pennsylvania who are much, much smarter than me. 

> Consider any algorithm which exploits during round *t* and explores during some later round *t'*.
> Consider the altered algorithm which explores during round *t* and exploits during round *t'*.
> This alteration leaves unaffected the values of exploitations at rounds earlier than *t* or later than *t'*
> and it monotonically improves the reward received from any exploitations in the interval (*t*, *t'*].
> The lemma follows by induction on all pairs (*t*, *t'*) of exploitation followed by exploration.

Even if that went over your head (which it definitely did for me on my first reading of the paper), the basic intuition should be easy: there's no point in exploiting before you explore, since you would've been better doing that exploitation after you had explored.

## 2. The Application to Humans

What happened in the podcast - and this is now something I think a lot - is the application of those sorts of algorithms to humans.

We often find ourselves facing optimization problems like the robot. We also deal with time constraints and nigh-infinite<sup>[1]</sup> potential options (notice that I swapped the idea of a *resource* for the idea of an *option* for the sake of application to humans, even though the underlying idea is the same). 

However, there are some distinguishing characteristics. And, of those, there are two that I find particularly important: heuristics, time ambiguity, and delay discounting.

To the first point, we often have heuristics that we can employ to get an idea of the value of an option *before* we do significant work in assessing it. For example, if I'm assessing the value of a book, I can very quickly look at its cover and read its title to get the idea of its general vibe. These heuristics also frequently come in layers: there are multiple heuristics we can use, with subsequent ones taking more time but giving you a more accurate picture of the utility of the option. I look at the cover, analyze the title, read the summary on the inside, check its overall rating on Goodreads, and *then* read a book. 

The second factor is time ambiguity. Unlike the robot who has a fixed time constraint that it's aware of, we fundamentally don't know our most limiting one - our lifespan. We have a general idea, but there still is a nonzero possibility that we could be wildly off. I suspect this makes us more exploitation-biased; we don't want to be stuck in the exploration phase when we die. Interestingly, this only holds if you suspect that you're going to die *earlier* than your expected lifespan. If you believe that you're going to die *later* than the average person, you should be *exploration*-biased relative to the average person.

The third factor is delay discounting. We value happiness **now** over happiness **later**. This almost entirely changes the decision calculus; by front-loading the exploration, you now decrease the utility of the later exploitation. The exact way in which this affects your choice of exploration/exploitation depends on your personal discounting function<sup>[2]</sup>.

![My best guess as to a generically optimal human exploration-exploitation curve]({static}/images/friendships-happiness/optimal.png)

This graph is what I'd guess an optimal exploration-exploitation curve looks like for humans. Obviously, the exact y-intercept or the x-axis scale aren't particularly important, as those are going to depend on the exact context (this graph is probably representative of, for example, exploration-exploitation of happiness-generating activities over time). But the shape is crucial: as time goes on, more energy is dedicated to *exploitation* as opposed to *exploration*, with that % energy *increasing at an increasing rate*. I.e., the derivative and the second derivative are both positive. I find this shape to intuitively stem from the above three factors, but I haven't sat down and rigorously thought about it. If I'm wrong, feel free to reach out and explain why.

<!---

## Friendships

This situation has an obvious correspondence with looking for friends. Much like robots pursuing an infinite amount of potential resources, there are essentially an infinite number of possible friends<sup>[2]</sup>. Each friend has a different value, corresponding to the happiness we gain from being friends with them. And we fundamentally have limited time — our lifespan — to maximize our happiness within.

## Heuristics

Unlike the robot, we have access to a variety of heuristics about the potential value of friends. There are heuristics we implicitly use before even talking to them: analyzing their habits (based on the context in which we meet them), their physical characteristics, their fashion, etc. And there are also heuristics we use during our first conversation with them: observing their humor, their eye contact, their intelligence, their laugh, their way of talking, etc.

So we, unlike the robot, scan ahead. Using the heuristics, we can establish an approximate floor for the value of a friendship; we say to ourselves that we *feel like* we could be friends with them.

But one thing I've realized recently is the problem with using such heuristics: **getting friendships is a problem that can't be solved with greedy algorithms using heuristics**<sup>[3]</sup>. At each instance, I'm best off by finding people who conform to my heuristics (which happens to disproportionately be extroverted nerdy guys), but the aggregate effect of that is having a friend group that's rather unbalanced in terms of interests — an echo chamber of personality. And so the happiness I get from each additional person who conforms decreases (i.e., there is attenuating marginal benefit).

As such, how can we best use the heuristics? One option is to simply disregard the heuristics altogether and make a conscious choice to attempt to befriend people equally. Another is to try to attenuate the importance of the heuristics over time. I find both of these pretty hard to implement personally, though.

## Network Effects

Besides our ability to use heuristics, there's also the presence of network effects; it's easier to become friends with someone if you are friends with their friends. 

So, from a certain perspective, the value a friend encapsulates *also* includes the value of the potential friends you could make by being friends with them.

From a consequentialist standpoint, there's no real problem with this mindset of being friends with someone because of their network; they gain a friend and you gain a friend, so everyone is better off. From their perspective, there is no difference between you being a friend for the sake of the happiness you gain from hanging out with *them specifically* versus you being a friend for the sake of the happiness you gain from hanging out with them *and* their network. In either instance, your incentives lead you to treat them like a close friend.

Still, viewing friends as a means instead of an end feels a bit morally suspect to me. In both instances, you evaluate friends based on the happiness they bring you; you (probably) wouldn't be friends with someone who, on net, makes you less happy. But including their network in that calculation feels strange, even though, rationally, you should.

I don't really know how to resolve this. Optimally, we'd incorporate the value of people's networks into our calculations of friendship, but that obviously seems a bit morally repugnant. The reconciliation is thus left as an exercise for the reader.

## Stickiness

Unlike the robot who can losslessly switch between resources, we have a certain stickiness with respect to friends. We form emotional attachments, and there are societal pressures to stick with them. 

After all, we find it difficult to leave friends who even make us on-net unhappy. It would be infinitely harder to leave friends that make us happy but *don't make us as happy as we could be with other friends*, even though that opportunity cost is a real cost of being friends with them. Combined with the fact that we have network effects, this implies that 
-->

# Footnotes
[1] Now, I've always been a bit annoyed by the term "nigh-infinite". Literally no number is nigh-infinite; every number you can possibly think of is, well, *infinitely* closer to 1 than it is to infinity. But, in this case, I find the term fairly appropriate. Our brains are [weak enough](https://theconversation.com/brains-are-bad-at-big-numbers-making-it-impossible-to-grasp-what-a-million-covid-19-deaths-really-means-179081) at perceiving large numbers that, for all intents and purposes, we basically just group them all as "super large" and increasingly lack any perception of scale as they continue to increase. And often we consume such a negligible proportion of the potential options that there may as well be an infinite number of them. For example, the article will later discuss the issue of finding friends. Obviously, there are not an infinite number of potential friends. But, considering the fact that we humans can only handle a [few hundred friendships at maximum](https://en.wikipedia.org/wiki/Dunbar%27s_number), there functionally is an infinite supply. At minimum, there's very little loss in application of the algorithm to instead assume that there *is* an infinite supply.

[2] This seems like a good place to transition into a tangential discussion about delay discounting functions. The ones I find most interesting are the time-inconsistent ones. Time-consistency is this idea of whether the decision you make depends on when the decision occurs. If it doesn't depend on when it occurs, it's time-consistent.

For example, consider the following two questions:
1. Would you prefer a dollar today or three dollars in a week?
2. Would you prefer a dollar in one year or three dollars in one year and one week?

Now, personally, I would take the three dollars in both scenarios. But I wouldn't fault someone for taking the one-dollar choice in (1); I can very easily imagine a rational person doing so. But I find myself hard-pressed to imagine a reasonable person taking the one-dollar choice in (2), even though both situations represent a 200% increase in value for a one-week delay. This implies that I view time-inconsistent delay discounting functions as *rational*. Perhaps you do too?