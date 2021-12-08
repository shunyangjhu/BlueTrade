import Vue from 'vue'
import Router from 'vue-router'
import Home from "../components/Home";

Vue.use(Router)

export default new Router({
    // mode: 'history',
    routes: [
        {
            path: '/',
            name: 'Default',
            redirect: '/home',
            component: Home
        },
        {
            path: '/home',
            name: 'Home',
            redirect: '/commodity_list',
            component: Home,
            children: [
                {
                    path: '/commodity_list',
                    name: 'CommodityListPage',
                    component: () => import('../components/commodity/CommodityListPage')
                },
                {
                    path: '/commodity_item',
                    name: 'CommodityItemPage',
                    component: () => import('../components/commodity/CommodityItemPage')
                },
                {
                    path: '/post',
                    name: 'CommodityPost',
                    component: () => import('../components/commodity/CommodityPost')
                },
                {
                    path: '/login',
                    name: 'Login',
                    component: () => import('../components/login/Login')
                },
                {
                    path: '/user_page',
                    name: 'UserPage',
                    redirect: '/user_page/dashboard',
                    component: () => import('../components/admin/dashboard/UserPage'),
                    children: [
                        {
                            path: '/user_page/dashboard',
                            name: 'UserDashboard',
                            component: () => import('../components/admin/dashboard/UserDashboard')
                        },
                        {
                            path: '/user_page/manage_post',
                            name: 'ManagePost',
                            component: () => import('../components/admin/tools/ManagePost')
                        },
                        {
                            path: '/user_page/bidding',
                            name: "BiddingComponent",
                            component: () => import('../components/admin/tools/BiddingComponent')
                        },
                        {
                            path: '/user_page/avatar',
                            name: "AvatarManagement",
                            component: () => import('../components/admin/tools/AvatarManagement')
                        },
                        {
                            path: '/user_page/security',
                            name: "SecurityManagement",
                            component: () => import('../components/admin/tools/SecurityManagement')
                        },
                        {
                            path: '/user_page/about_us',
                            name: "AboutUs",
                            component: () => import('../components/helpcenter/AboutUs')
                        },
                        {
                            path: '/user_page/contact_us',
                            name: "ContactUs",
                            component: () => import('../components/helpcenter/ContactUs')
                        },
                        {
                            path: '/user_page/common_questions',
                            name: "FAQ",
                            component: () => import('../components/helpcenter/FAQ')
                        }
                    ]
                },
            ]
        },
        {
            path: '/register',
            name: 'Register',
            component: () => import('../components/login/Register')
        },

    ]
})
