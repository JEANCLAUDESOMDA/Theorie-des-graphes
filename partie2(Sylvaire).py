    def visualiser(self):
        plt.figure(figsize=(18, 14))
        pos = nx.spring_layout(self.G, k=6, seed=47, iterations=100)
        for node in pos:
            pos[node] = pos[node] * 2
        for node in self.G.nodes():
            if 'type' not in self.G.nodes[node]:
                self.G.nodes[node]['type'] = 'Non défini'
        types = {data['type'] for _, data in self.G.nodes(data=True)}
        palette = plt.cm.Set3.colors
        type_to_color = {typ: palette[i % len(palette)] for i, typ in enumerate(types)}
        for typ, color in type_to_color.items():
            nodes = [node for node, data in self.G.nodes(data=True) if data['type'] == typ]
            nx.draw_networkx_nodes(
                self.G, pos, 
                nodelist=nodes,
                node_color=[color] * len(nodes),
                node_size=3000,
                label=typ,
                alpha=0.8
            )

        # Labels avec (personne) si applicable
        labels_noeuds = {}
        types_personne = {"FOURNISSEUR", "CHAUFFEUR", "VOYAGEUR", "RECEPTEUR"}
        for node, data in self.G.nodes(data=True):
            label = node
            if data['type'] in types_personne:
                label += " (personne)"
            labels_noeuds[node] = label
        nx.draw_networkx_labels(
            self.G, pos,
            labels=labels_noeuds,
            font_size=10,
            font_weight='bold',
            verticalalignment='center'
        )

        nx.draw_networkx_edges(
            self.G, pos,
            arrowstyle='->',
            arrowsize=25,
            edge_color='darkblue',
            width=2,
            alpha=0.7,
            connectionstyle="arc3,rad=0"
        )
        edge_labels = nx.get_edge_attributes(self.G, 'label')
        nx.draw_networkx_edge_labels(
            self.G, pos,
            edge_labels=edge_labels,
            font_size=8,
            font_color='darkred',
            font_weight='bold',
            label_pos=0.5,
            bbox=dict(boxstyle="round,pad=0.3", facecolor='white', alpha=0.8, edgecolor='none')
        )
        plt.legend(
            loc='upper left',
            bbox_to_anchor=(1.02, 1),
            ncol=1,
            fontsize=10,
            frameon=True,
            fancybox=True,
            shadow=True
        )
        plt.title("Graphe Orienté des Relations", fontsize=16, fontweight='bold', pad=20)
        plt.axis('off')
        plt.tight_layout()
        plt.show()