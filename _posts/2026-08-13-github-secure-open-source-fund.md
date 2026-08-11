---
layout: post
title: "What I learned securing Sniffnet with the GitHub Secure Open Source Fund"
share-title: "What I learned securing Sniffnet with the GitHub Secure Open Source Fund"
nav-title: News
thumbnail-img: /assets/img/post/github-secure-open-source-fund/cover.png
tags: [security]
github-discussion: TODO
---

I've always built Sniffnet with a security-first mindset, and today I'm thrilled to announce a major milestone
faithfully aligned with that philosophy: Sniffnet recently took part in the <a target="_blank" rel="noopener" href="https://github.com/open-source/github-secure-open-source-fund">GitHub Secure Open Source Fund</a>!
<div align="center">
    <a target="_blank" rel="noopener" href="https://github.com/open-source/github-secure-open-source-fund">
        <img width="70%" title="GitHub Secure Open Source Fund" alt="GitHub Secure Open Source Fund" style="border-radius: 15px" src="{{ 'assets/img/post/github-secure-open-source-fund/cover.png' | relative_url }}">
    </a>
</div>
Backed by industry giants like Microsoft, Stripe, 1Password, and Shopify,
it's a dedicated initiative focused on improving the security and sustainability of critical open-source software.<br><br>
In this blog post, I'll share how the program made Sniffnet more secure, and walk you through the steps you can follow to do the same.<br><br>
After all, one of the most important lessons I'm taking away from this experience is that security is a joint effort of the whole
community: each project is a tiny piece of a bigger puzzle and no one can be completely safe if the rest of the ecosystem isn't.

<hr>

### The GitHub Secure Open Source Fund program

The program's mission is to secure open source software that is widely used and critical to the modern stack.

It consists of an immersive 3-week sprint that provides each onboarded project with $10k in funding, hands-on training, and mentorship to help maintainers
understand that security is a baseline requirement, not a nice-to-have.<br>
The sprint is curated by the <a target="_blank" rel="noopener" href="https://securitylab.github.com">GitHub Security Lab</a> and delivered by a team of security experts.

Sniffnet and other TODO projects joined the fourth session of the program this past April,
and selected participants were asked not to share the news until today's <a target="_blank" rel="noopener" href="TODO-OFFICIAL-ANNOUNCEMENT-URL">official announcement</a>,
to avoid any potential exposure and to focus on securing our codebases.

[pic: TODO]

The best part?<br>
The program isn't only about learning and theory: it's designed as a series of practical steps
that have to be taken to satisfy outcome-driven goals and verified security requirements, having a tangible impact on the project and its users.

<hr>

### Security as a priority

As mentioned in the introduction, I've always cared about securing Sniffnet:
this website's homepage states that _"one of the top priorities is to protect data privacy and system integrity"_,
and not long ago the project underwent an independent <a href="{{ 'news/security-audit' | relative_url }}">security audit</a>.

And... can you guess the specialization of my Computer Science Master's degree?<br>
Cybersecurity, of course!

Despite having been in the field for a while,
I had never been exposed to a structured security program like the Secure Open Source Fund,
and I was amazed by the number of tools that GitHub natively offers to make code more robust.

Unfortunately, the reality is that **too often security is deferred** to the end of the development cycle or,
even worse, only considered in a moment of panic after a vulnerability is discovered.<br>
A shift in mentality is therefore needed to proactively design and plan security,
rather than downgrading it to a mere reactive countermeasure.

<div align="center">
    <img width="80%" title="Sniffnet's quote from the program" alt="Sniffnet's quote from the program" style="border-radius: 15px" src="{{ 'assets/img/post/github-secure-open-source-fund/quote.png' | relative_url }}">
</div>

I feel a responsibility to amplify security awareness by sharing the knowledge and best practices I learned,
so that other developers can take inspiration and apply similar measures in their own projects.

<hr>

### Incident response planning and threat modeling

Before even worrying about concrete measures, the first step is to define a clear security plan.

Planning is crucial for two main reasons:
1. when something bad happens (it will happen, sooner or later), having a robust strategy ready will let you act calmly and effectively even under pressure
2. outlining the most critical assets of your project before they are compromised will help you focus your efforts on what really matters

Point 1 is addressed by **incident response planning** (IRP), which consists of defining the roles, responsibilities, and an ordered set of actions to follow in case of a security incident.<br>
The goal is to have a procedure in mind to contain the effects of the incident and restore normal operations as quickly as possible.<br>
For a detailed IRP document, you can check out Sniffnet's <a target="_blank" rel="noopener" href="https://github.com/GyulyVGC/sniffnet/blob/main/INCIDENT_RESPONSE.md"><code>INCIDENT_RESPONSE.md</code></a>.

Point 2 is instead a matter of **threat modeling**, the process of cataloging the threats that specific assets of your system may be exposed to.<br>
To identify common types of threats, we used the <a target="_blank" rel="noopener" href="https://learn.microsoft.com/en-us/azure/security/develop/threat-modeling-tool-threats">STRIDE</a> framework, which classifies threats into six categories: Spoofing, Tampering, Repudiation, Information Disclosure, Denial of Service, and Elevation of Privilege.<br>
A truly exhaustive threat model would come up with a huge two-dimensional matrix of _threats × assets_, which is something complex to do and hard to maintain, especially for large projects.<br>
For this reason, rather than postponing the process indefinitely, it's advisable to start by analyzing the most critical assets of your system, ranked by likelihood and impact of exploitation, and gradually expand the coverage over time.<br>
If you are curious to see how this turned out for Sniffnet you can have a look at our first <a target="_blank" rel="noopener" href="https://github.com/GyulyVGC/sniffnet/blob/main/THREAT_MODEL.md"><code>THREAT_MODEL.md</code></a>.

The two documents mentioned above are even more effective if paired with a **security policy** that describes how to report vulnerabilities and how the maintainers handle them, so that contributors and users are aware of the security measures in place.<br>
You can consult Sniffnet's security policy in our <a target="_blank" rel="noopener" href="https://github.com/GyulyVGC/sniffnet/blob/main/SECURITY.md"><code>SECURITY.md</code></a>.
  
<hr>

### Practical security measures and tools

With a clear security design in place, it's finally time to get our hands dirty.

This is where the program really shines, in my opinion,
as it provides a set of **actionable measures** that have a real impact and yet can be rolled out in a relatively short time.<br>
Given their benefit-to-effort ratio, I think anyone should adopt them as a baseline for their open source work.

Sniffnet already had the most relevant ones covered, but the program helped me close a few gaps here and there.<br>
The list is long, so here I'll limit myself to a table of security-boosting tools provided by GitHub, with a short description of their purpose and a link to the corresponding official documentation.


| Measure                                                                                                                                                                                                                                                     | What it is and why it's useful                                                                                                                                                                                          |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <a target="_blank" rel="noopener" href="https://docs.github.com/en/code-security/how-tos/secure-your-secrets/detect-secret-leaks/enabling-secret-scanning-for-your-repository">Secret scanning</a>                                                          | Scans the repository for leaked credentials such as API keys and tokens, and alerts you when one is found.<br>Its companion _push protection_ also blocks commits containing secrets before they even reach the remote. |
| <a target="_blank" rel="noopener" href="https://docs.github.com/en/code-security/how-tos/find-and-fix-code-vulnerabilities/configure-code-scanning/configure-code-scanning">Code scanning</a>                                                               | Uses CodeQL to perform a rule-based static analysis of your source code and GitHub Actions workflows to find vulnerabilities and code smells.                                                                           |
| <a target="_blank" rel="noopener" href="https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/creating-rulesets-for-a-repository">Repository rulesets</a>                                            | Define who can push what, and where.<br>They prevent accidental (or malicious) direct pushes and protect tags so that published releases can't be silently rewritten.                                                   |
| <a target="_blank" rel="noopener" href="https://docs.github.com/en/code-security/how-tos/secure-your-supply-chain/establish-provenance-and-integrity/prevent-release-changes">Immutable releases</a>                                                        | Locks a release: its git tag stays pinned to the same commit, and its assets can no longer be modified.<br>Without it, anyone who gets hold of a maintainer account could tamper with published binaries.               |
| <a target="_blank" rel="noopener" href="https://docs.github.com/en/code-security/how-tos/report-and-fix-vulnerabilities/configure-vulnerability-reporting/configuring-private-vulnerability-reporting-for-a-repository">Private vulnerability reporting</a> | Gives security researchers a confidential channel to responsibly disclose vulnerabilities, instead of opening a public issue that would expose the vulnerability to attackers.                                          |
| <a target="_blank" rel="noopener" href="https://docs.github.com/en/code-security/tutorials/secure-your-dependencies/dependabot-quickstart">Dependabot alerts</a>                                                                                            | Notify you when one of your dependencies is affected by a known vulnerability, and automatically open a pull request that bumps it to a patched version.                                                                |
| <a target="_blank" rel="noopener" href="https://docs.github.com/en/authentication/securing-your-account-with-two-factor-authentication-2fa/configuring-two-factor-authentication">Multi-factor authentication</a>                                           | Requires maintainers to prove their identity with a second factor to prevent account takeovers.                                                                                                                         |
| <a target="_blank" rel="noopener" href="https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens">Fine-grained access tokens</a>                                                                 | Grant every token only the permissions it strictly needs.<br>Using the least-privilege approach reduces the blast radius of a compromised workflow or leaked token.                                                     |

As anticipated, implementing these measures is a good starting point for general project health, but to this day,
targeted testing and fuzzing still remain the most effective ways to find flaws specific to your codebase.<br>
Today Sniffnet is equipped with a decent set of unit tests, but I've already <a target="_blank" rel="noopener" href="https://github.com/GyulyVGC/sniffnet/issues/1038">planned more extensive integration tests</a>,
concerning both the core packet parsing logic and the GUI layer.

<hr>

### Wrapping up

So... _is security fixed forever?_

You already know the answer to this question, and it's... \*_drum roll_\*... **NO!**

Security is a bit like life: you can give it one hundred percent and do everything right,
but something can still go sideways.<br>
In a world where Murphy's law reigns supreme (_"anything that can go wrong will go wrong"_),
what we can do is **be prepared for it**, and I must thank the cybersecurity courses
I took at university and the GitHub Secure Open Source Fund for instilling this kind of mentality in me.

And don't forget we're in the era of LLM-generated code,
where human errors happen at superhuman speed: AI makes coding faster, but it can introduce vulnerabilities faster too.

This is why I also updated Sniffnet's <a target="_blank" rel="noopener" href="https://github.com/GyulyVGC/sniffnet/blob/main/CONTRIBUTING.md">Contributing Manifesto</a> to reflect the recent paradigm shifts.<br>
I structured it as 10 rules that contributors are expected to observe before submitting pull requests, and the first one is:
> 1. purely LLM-generated code contributions are strongly discouraged and will most likely be rejected: you must understand and be able to defend every line you submit, and disclose AI assistance if any was used in the process 

Even though I feel that Sniffnet is getting more and more secure and reliable over time,
as these lines have hopefully shown, this is a never-ending journey.<br>
I'm eager to pursue further independent audits in the near future, and to never stop learning about new attack vectors.

Because in the world of network monitoring, keeping an eye on traffic is only half the battle:
the tool you use must be as secure as the network it monitors 🫡