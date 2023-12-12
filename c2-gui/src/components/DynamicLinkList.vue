<template>
    <div class="container d-flex justify-content-center align-items-center vh-100">
        <ul class="list-group">
            <li v-for="(link, index) in links" :key="index" class="list-group-item">
                <a :href="link.url" target="_blank">{{ link.title }}</a>
            </li>
        </ul>
    </div>
</template>

<script>
export default {
    name: 'DynamicLinkList',
    data() {
        return {
            links: [], // Array to store links from the API response
        };
    },
    mounted() {
        // Fetch links from the API when the component is mounted
        this.fetchLinks();
    },
    methods: {
        async fetchLinks() {
            try {
                // Make an API request using Axios
                const response = await this.$axios.get('http://localhost:8880/clients');
                // Assuming the API response is an array of link objects with 'title' and 'url' properties
                this.links = response.data;
            } catch (error) {
                console.error('Error fetching links:', error);
            }
        },
    },
};
</script>