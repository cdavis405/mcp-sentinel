# MCP Sentinel - Task List

> Track progress, maintain context, stay focused.

---

## 📍 Where We've Been

### ✅ Completed

| Date | Milestone | Notes |
|------|-----------|-------|
| 2024-12 | Forked cml-mcp | Base MCP server for CML interaction |
| 2024-12 | Basic lab deployment working | Can create labs, add nodes via MCP |
| 2024-12 | YAML topology definitions | `designs/enterprise_v1.yaml` created |
| 2024-12 | Deployment script | `deploy_lab.py` for importing topologies |
| 2024-12 | README vision complete | Bleeding-edge goals, change management philosophy documented |

### 📝 Key Decisions Made

- **Change Management is core** — Blast radius, command preview, and approval required for all changes
- **Phoenix Project philosophy** — Inspired by the book; governance over chaos
- **Multi-stakeholder future** — Building toward group chat approvals (Slack/Teams + AI agent)
- **End-to-end scope** — Not just network; full stack from AD/GPO to employee laptop

---

## 🎯 Where We're Going

### Phase 2: Identity & Access 🔄 CURRENT

#### Active Directory Infrastructure
- [ ] Deploy Windows Server in CML
- [ ] Promote to Domain Controller
- [ ] Configure DNS (AD-integrated)
- [ ] Configure DHCP (AD-integrated)
- [ ] Create OU structure (IT, Engineering, Sales, Contractors)
- [ ] Create test users and groups
- [ ] Build baseline GPOs

#### Certificate Services
- [ ] Deploy Enterprise CA on Windows Server
- [ ] Create certificate template for 802.1X (Computer + User)
- [ ] Configure auto-enrollment via GPO
- [ ] Test certificate issuance to domain-joined machine

**Exit Criteria:** Domain-joined machine receives certificate automatically via GPO.

---

### Phase 3: Network Access Control

#### Cisco ISE Deployment
- [ ] Deploy ISE node in CML
- [ ] Initial setup (admin, NTP, DNS)
- [ ] Add network devices (switches) to ISE
- [ ] Configure RADIUS authentication
- [ ] Create authentication policies (802.1X, MAB fallback)
- [ ] Create authorization profiles (VLANs, dACLs)
- [ ] Test RADIUS authentication from switch

#### 802.1X on Network Devices
- [ ] Configure 802.1X on access switch ports
- [ ] Test wired authentication (EAP-TLS with certificate)
- [ ] Configure MAB fallback for non-802.1X devices
- [ ] Test guest portal flow

**Exit Criteria:** Laptop authenticates via 802.1X, gets correct VLAN/ACL from ISE.

---

### Phase 4: Network Infrastructure

#### SD-WAN Fabric
- [ ] Deploy vManage in CML
- [ ] Deploy vBond in CML
- [ ] Deploy vSmart in CML
- [ ] Configure root CA for SD-WAN certificates
- [ ] Deploy vEdge/cEdge at "HQ" site
- [ ] Deploy vEdge/cEdge at "Branch" site
- [ ] Establish OMP peering
- [ ] Test overlay connectivity
- [ ] Configure basic control policies

#### Underlay Network
- [ ] Configure OSPF/BGP underlay
- [ ] Simulate MPLS transport
- [ ] Simulate Internet transport
- [ ] Configure QoS policies

**Exit Criteria:** SD-WAN overlay functional between HQ and Branch; traffic flows over correct path.

---

### Phase 5: Security & Segmentation

- [ ] Deploy perimeter firewall
- [ ] Configure zone-based policies
- [ ] Implement TrustSec SGTs on switches
- [ ] Configure ISE SGT assignment
- [ ] Test micro-segmentation (Engineering can't reach HR VLAN)

**Exit Criteria:** SGT-based segmentation enforced; policy traced across ISE → Switch.

---

### Phase 6: Employee Onboarding Flow 🔥 THE GOAL

- [ ] New laptop boots, joins domain
- [ ] Certificate auto-enrolled
- [ ] Laptop connects to wired port
- [ ] 802.1X triggers, EAP-TLS authenticates
- [ ] ISE returns authorization (VLAN, SGT, dACL)
- [ ] GPO applies desktop config
- [ ] User launches Teams, traffic routed via SD-WAN
- [ ] **Full flow validated end-to-end**

**Exit Criteria:** Zero-touch laptop → fully operational → verified via LLM.

---

### Phase 7: Day 2 Operations

- [ ] LLM can query ISE for auth failures
- [ ] LLM can check AD account status
- [ ] LLM can verify certificate validity
- [ ] LLM can trace traffic path across SD-WAN
- [ ] LLM can correlate policy across AD → ISE → Switch → FW → SD-WAN
- [ ] **"Why can't Sarah authenticate?" → Root cause via conversation**

**Exit Criteria:** Troubleshooting complex issues via natural language.

---

## 🔥 Bleeding-Edge Challenges

| Challenge | Phase | Status |
|-----------|-------|--------|
| Full 802.1X with EAP-TLS | 2-3 | ⬜ Not Started |
| ISE + TrustSec SGTs | 3-5 | ⬜ Not Started |
| SD-WAN Fabric from Scratch | 4 | ⬜ Not Started |
| Zero-Touch Employee Onboarding | 6 | ⬜ Not Started |
| LLM-Driven Troubleshooting | 7 | ⬜ Not Started |
| Cross-Domain Policy Correlation | 7 | ⬜ Not Started |

---

## 📋 Next Actions

> Update this section at the start of each work session.

**Current Focus:** Phase 2 - Identity & Access

**Next Step:** Deploy Windows Server in CML

**Blockers:** None currently

---

## 🗒️ Session Notes

### 2024-12-06
- Created TASKS.md to track progress
- README.md updated with full vision
- Change management philosophy documented
- Ready to start Phase 2

---

*Last Updated: 2024-12-06*
