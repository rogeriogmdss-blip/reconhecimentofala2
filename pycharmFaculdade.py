class User:
    def __init__(self, user_id, data):
        self._user_id = user_id
        self._data = data

    # Getters
    def get_user_id(self):
        return self._user_id

    def get_data(self):
        return self._data

    # Setters
    def set_data(self, new_data):
        self._data = new_data

import networkx as nx
import networkx.algorithms.community as nx_comm

class SocialNetwork:
    def __init__(self):
        self.graph = nx.Graph()

    def add_user(self, user_id, user_data):
        self.graph.add_node(user_id, data=user_data)

    def remove_user(self, user_id):
        self.graph.remove_node(user_id)

    def connect_users(self, user1_id, user2_id):
        self.graph.add_edge(user1_id, user2_id)

    def disconnect_users(self, user1_id, user2_id):
        self.graph.remove_edge(user1_id, user2_id)

    def find_communities(self):
        # Algoritmo de detecção de comunidades: greedy modularity
        communities = nx_comm.greedy_modularity_communities(self.graph)
        return [list(community) for community in communities]

    def user_centralities(self, method='degree'):
        if method == 'degree':
            return nx.degree_centrality(self.graph)
        elif method == 'betweenness':
            return nx.betweenness_centrality(self.graph)
        elif method == 'closeness':
            return nx.closeness_centrality(self.graph)
        elif method == 'eigenvector':
            return nx.eigenvector_centrality(self.graph)
        else:
            raise ValueError("Método de centralidade inválido.")

    def analyze_subgraph(self, user_ids):
        subgraph = self.graph.subgraph(user_ids)
        return {
            "nodes": list(subgraph.nodes(data=True)),
            "edges": list(subgraph.edges())
        }


# Testando as funcionalidades da rede social
if __name__ == "__main__":
    # Criando a rede social
    sn = SocialNetwork()

    # Criando usuários
    u1 = User("u1", {"nome": "Ana", "interesses": ["música", "viagem"]})
    u2 = User("u2", {"nome": "Bruno", "interesses": ["esportes", "tecnologia"]})
    u3 = User("u3", {"nome": "Carlos", "interesses": ["fotografia"]})
    u4 = User("u4", {"nome": "Diana", "interesses": ["livros", "arte"]})
    u5 = User("u5", {"nome": "Elisa", "interesses": ["teatro", "moda"]})

    # Adicionando usuários à rede
    sn.add_user(u1.get_user_id(), u1.get_data())
    sn.add_user(u2.get_user_id(), u2.get_data())
    sn.add_user(u3.get_user_id(), u3.get_data())
    sn.add_user(u4.get_user_id(), u4.get_data())
    sn.add_user(u5.get_user_id(), u5.get_data())

    # Conectando usuários
    sn.connect_users("u1", "u2")
    sn.connect_users("u2", "u3")
    sn.connect_users("u3", "u4")
    sn.connect_users("u4", "u5")
    sn.connect_users("u1", "u5")  # Rede com ciclo

    # Calculando centralidades
    print("\nCentralidade (degree):")
    print(sn.user_centralities("degree"))

    print("\nCentralidade (betweenness):")
    print(sn.user_centralities("betweenness"))

    # Detectando comunidades
    print("\nComunidades detectadas:")
    communities = sn.find_communities()
    for i, community in enumerate(communities):
        print(f"Comunidade {i+1}: {community}")

    # Analisando subgrafo
    print("\nSubgrafo (u1, u2, u3):")
    subgraph_info = sn.analyze_subgraph(["u1", "u2", "u3"])
    print("Nós:", subgraph_info["nodes"])
    print("Arestas:", subgraph_info["edges"])

    # Removendo conexão
    sn.disconnect_users("u1", "u5")

    # Removendo usuário
    sn.remove_user("u3")
    

   

    
    

  
