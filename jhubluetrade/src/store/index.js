import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex);

export default new Vuex.Store({
    state: {
        email: window.localStorage.getItem('email') == null ? '' : JSON.parse(window.localStorage.getItem('email' || '[]')),
    },
    mutations: {
        login (state, data) {
            state.email = data;
            window.localStorage.setItem('email', JSON.stringify(data));
        },
        logout(state) {
            state.email = '';
            window.localStorage.removeItem('email');
        }
    }
})