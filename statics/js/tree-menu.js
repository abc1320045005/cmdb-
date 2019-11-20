var ul = `<ul class="treeview-menu" style="display: block;">`
let hasNot = ''
let li = []

function displayNode(nodes) {
    for (node of nodes) {
        if (node.sub_node.length === 0) {
            hasNot = node.node_name
            li.push(`<li><a href="/cmdb/server-detail/?node_id=${node.id}"><i class="fa fa-circle-o"></i>
                            ${hasNot}</a>
                        </li>`)

        } else {

            has = node.node_name
            li.push(`<li class="treeview menu-open" style="height: auto;">
                        <a href="#"><i class="fa fa-circle-o"></i>
                            ${has}
                          <span class="pull-right-container">
                            <i class="fa fa-angle-left pull-right"></i>
                          </span>
                        </a>`)
            li.push(ul)

            displayNode(node.sub_node)
            li.push('</ul>')
            li.push('</li>')
        }

    }
    return li
}
