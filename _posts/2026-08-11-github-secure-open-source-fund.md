---
layout: post
title: "Sniffnet security levels up with the GitHub Secure Open Source Fund"
share-title: "Sniffnet security levels up with the GitHub Secure Open Source Fund"
nav-title: News
thumbnail-img: /assets/img/post/github-secure-open-source-fund/cover.png
tags: [security]
github-discussion: XXXX
---

I've always built Sniffnet with a security-first mindset, and today I'm thrilled to announce a major milestone
faithfully aligned with such philosophy: Sniffnet has recently been part of the GitHub Secure Open Source Fund!<br><br>
Backed by industry giants like Microsoft, 1Password, Shopify, and Stripe,
the GitHub Secure Open Source Fund is a dedicated initiative focused on improving the security and sustainability of critical open-source software.<br><br>
In this blog post, I'll share how the program made Sniffnet more secure, and guide you through actionable steps you can follow to do the same.<br><br>
After all, one of the most important lessons I take away from this experience is that security is a joint effort of the whole
community: each project is a tiny piece of a bigger puzzle and no one can be completely safe if the rest of the ecosystem isn't.

<hr>

### The GitHub Secure Open Source Fund program

The program's mission is to secure open source software that is widely used and critical to the modern stack.

It consists of an immersive 3-week sprint that provides $10k funding to each onboarded project, hands-on training, and mentorship to help maintainers
understand that security is a baseline requirement, not a nice-to-have.<br>
The sprint is curated by the GitHub security Lab () and delivered by a team of security experts.

[pic]

Sniffnet and other x projects joined the fourth session of the program the past April,
and selected participants were asked not to share the news until today's official announcement,
to avoid any potential exposure and to focus on securing our codebases.

[pic]

The best part?<br>
The GitHub Secure Open Source Fund isn't only about learning and theory: the program is designed as a series of practical steps
that have to be taken to satisfy outcome-driven goals and verified security requirements, leaving a tangible impact on the project and its users.

<hr>

### Security as a priority

As mentioned in the introduction, I've always cared about securing Sniffnet:
this website's homepage states that _"one of the top priorities is to protect data privacy and system integrity"_
and not long ago the project underwent an independent security audit ().

And... can you guess the specialization of my Computer Science Master's degree?<br>
Cybersecurity, of course!

Despite being in the environment for a while,
I had never been exposed to a structured security program like the Secure Open Source Fund,
and I was amazed by the amount of tools that GitHub natively offers to make code more robust.

But unfortunately, the reality is that too often security is deferred to the end of the development cycle or,
even worse, it's only considered in a moment of panic after a vulnerability is discovered.<br>
A shift in mentality is therefor needed to proactively design and plan security,
rather than downgrading it to a mere reactive countermeasure.

Given these premises, I feel the responsibility to amplify security awareness by sharing the knowledge and best practices I learned,
so that other developers can take inspiration and execute similar actions in their own projects.

<hr>

### Incident response planning and threat modeling

Before even worrying about practical measures, the first step is to define a clear security plan.

Planning is crucial for two main reasons:
1. when something bad happens (it will happen, sooner or later), having a robust strategy in place will make you act calmly and effectively evn under pressure
2. outlining the most critical assets of your project before they are compromised will help you prioritize your efforts on what really matters

Point 1 is implemented through **incident response planning** (IRP), and consists of defining the roles, responsibilities, and an ordered set of actions to follow in case of a security incident.<br>
The goal is to have in mind a procedure to contain the impact of the incident and restore normal operations as quickly as possible.<br>
For a detailed IRP document, you can check out and take inspiration from Sniffnet's [`INCIDENT_RESPONSE.md`]().

Point number 2 is instead known as **threat modeling**, which is the process that catalogues the threats that specific assets of your system may be exposed to.<br>
To identify common types of threats, we used the opinionated STRIDE framework, which classifies threats into six categories: Spoofing, Tampering, Repudiation, Information Disclosure, Denial of Service, and Elevation of Privilege.<br>
A truly exhaustive threat model would come up with a huge bidimensional matrix of the _threats X assets_, which is something complex to do and hard to maintain especially for large projects.<br>
For this reason, rather than permanently procrastinating the process, it's advisable to start analyzing the most critical assets of your system by likelihood and impact of exploitation, and gradually expand the coverage over time.<br>
If you are curious to see how this turned out for Sniffnet you can give a look at our first [`THREAT_MODEL.md`]().

The two documents mentioned above are even more effective if paired with a **security policy** that describes how to report vulnerabilities and how the maintainers handle them, so that contributors and users are aware of the security measures in place.<br>
You can consult Sniffnet's security policy in our [`SECURITY.md`]().
  
<hr>

### Practical security measures and tools

After having a clear security design in place, it's finally time to get our hands dirty with the practical stuff.

In my opinion, this is where the GitHub Secure Open Source Fund program really shines,
as it provides a set of actionable measures that have a real impact and yet can be implemented in a relatively short time.<br>
Given their benefit-to-effort ratio, I think anyone should implement them as a baseline for their open source work.

Sniffnet already had some of the most relevant ones in place, but the program helped me to close some gaps here and there.<br>
The TODO list is long, so herein I'll limit myself to a table of security-boosting tools provided by GitHub with a short description of their purpose and a link to the corresponding official documentation.


| Measure                             | What it is and why it's useful                                                                                                                                                                                                                                                                                                                                                                                                    | How to enable it                                                                                                                                                                                    |
|-------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Secret scanning**                 | Scans the repository (including its full Git history) for leaked credentials such as API keys and tokens, and alerts you when one is found. Its companion _push protection_ goes one step further and blocks commits containing secrets before they even reach the remote, which is the only way to avoid the painful key rotation dance.                                                                                         | [Link](https://docs.github.com/en/code-security/how-tos/secure-your-secrets/detect-secret-leaks/enabling-secret-scanning-for-your-repository)                                                       |
| **Code scanning**                   | Statically analyzes your source code to find vulnerabilities and coding errors before they are shipped. GitHub's CodeQL engine treats code as data to be queried, and can scan both your application code and your GitHub Actions workflows. Remember to opt for the `security-extended` query suite to catch a wider set of issues.                                                                                              | [Link](https://docs.github.com/en/code-security/how-tos/find-and-fix-code-vulnerabilities/configure-code-scanning/configure-code-scanning)                                                          |
| **Repository rulesets**             | Define who can push what, and where. Requiring pull requests, reviews, and passing status checks on the default branch prevents accidental (or malicious) direct pushes, and protects tags so that published releases can't be silently rewritten.                                                                                                                                                                                | [Link](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/creating-rulesets-for-a-repository)                                             |
| **Immutable releases**              | Locks a published release: its Git tag stays pinned to the same commit, and its assets can no longer be modified or deleted. Without it, anyone who gets hold of a maintainer account can quietly swap a binary under an existing release, and every user downloading it afterwards would get the tampered version.                                                                                                               | [Link](https://docs.github.com/en/code-security/how-tos/secure-your-supply-chain/establish-provenance-and-integrity/prevent-release-changes)                                                        |
| **Private vulnerability reporting** | Gives security researchers a confidential channel to disclose vulnerabilities directly on your repository, instead of opening a public issue that would expose your users before a fix is available. It's a single toggle, and it removes every excuse for irresponsible disclosure.                                                                                                                                              | [Link](https://docs.github.com/en/code-security/how-tos/report-and-fix-vulnerabilities/configure-vulnerability-reporting/configuring-private-vulnerability-reporting-for-a-repository)              |
| **Dependabot alerts and updates**   | Notifies you when one of your dependencies is affected by a known vulnerability, and automatically opens pull requests that bump it to a patched version. Given that the vast majority of a modern codebase is third-party code, this is where a huge share of your attack surface actually lives.                                                                                                                                | [Link](https://docs.github.com/en/code-security/tutorials/secure-your-dependencies/dependabot-quickstart)                                                                                           |
| **Multi-factor authentication**     | Requires maintainers and contributors with write access to prove their identity with a second factor. A stolen password is worth nothing without it, and account takeover of a single maintainer is one of the cheapest ways to compromise a whole project and its downstream users.                                                                                                                                              | [Link](https://docs.github.com/en/authentication/securing-your-account-with-two-factor-authentication-2fa/configuring-two-factor-authentication) |
| **Least privilege for tokens**      | Grant every token only the permissions it strictly needs. In workflows, the `permissions` key restricts the scope of the automatically provided `GITHUB_TOKEN` (start from `contents: read` and add from there); outside of workflows, prefer fine-grained personal access tokens limited to specific repositories and with a short expiration. This way, a compromised workflow or leaked token has a very limited blast radius. | [Link](https://docs.github.com/en/actions/how-tos/security-for-github-actions/security-guides/use-github_token-in-workflows)                                                                        |


<hr>

### Wrapping up

So did we fix security forever?

You already know the answer to this question, and it's... \*_drum rolls_\*... NO!

Security is a bit just like life: you can give it your one hundred percent and do everything right,
but something can still go sideways.<br>
In a world where Murphy's law is always around the corner (_"anything that can go wrong will go wrong"_),
what we can do is to be prepared for it, and I must thank the Cybersecurity courses
I followed at university and the GitHub Secure Open Source Fund for having instilled this kind of mentality in me.

And don't forget we're in the era of LLM-generated code,
where we have human errors at superhuman speed: AI makes coding faster but can also introduce vulnerabilities faster.

This is why I also updated Sniffnet's Contributing Manifesto to reflect the recent shifts in paradigm.<br>
I structured it as 10 rules that shall be respected by contributors before submitting pull requests, and the first one is:
> 1. purely LLM-generated code contributions are strongly discouraged and will most likely be rejected: you must understand and be able to defend every line you submit, and disclose AI assistance if any was used in the process 

Even if I feel that Sniffnet is getting always more secure and reliable over time,
as you read along the lines I believe security is a never-ending trip, and I'm eager to get
other independent security audits in the near future and never stop learning about new class of attacks.

Because in the world of network monitoring, keeping an eye on traffic is only half the battle:
the tool you use must be as secure as the network it monitors 